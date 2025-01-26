import subprocess
import time
import os
import asyncio
from urllib.parse import urlparse
from scripts.crawler import *
from scripts.selenium import *
from scripts.injection_log import *

injection_found = False
injection_log = []
start_time = 0
detected_info = {"WEB_SERVER": None, "TECHNOLOGY": None, "DBMS": None}

async def core(input_url: str, strength: int, threads: int, flush_session: bool, verbose: bool, manual_command: str):
    global start_time
    queue = asyncio.Queue()

    try:
        timeout = 10  # Lower -> Fast, less accurate. Higher -> Slow, more accurate

        if not input_url:
            yield "Enter a valid URL"
            return
        else:
            input_url = ensure_url_scheme(input_url)

        # Strength Mapping
        strength_mapping = {
            1: (1, 1),
            2: (2, 2),
            3: (3, 3),
            4: (4, 3),
            5: (5, 3)
        }
        level, risk = strength_mapping.get(strength, (3, 3))

        yield f"URL given: {input_url}"
        start_time = time.time()

        async for message in process_targets(input_url, level, risk, threads, timeout, flush_session, verbose, manual_command, queue):
            yield message

    except ValueError:
        yield "Invalid input"

async def process_targets(input_url, level, risk, threads, timeout, flush_session, verbose, manual_command, queue):
    global injection_found
    global start_time
    global injection_log

    await asyncio.sleep(0.1)  # Allow event loop to switch tasks

    yield(f"\nCrawling and analyzing {input_url} for vulnerabilities...")

    # Ensure 'crawler' is awaited and communicates via queue
    await init_queue(queue)
    found_urls = await crawler(input_url)

    while not queue.empty():
        yield await queue.get()

    verbosity = 3 if verbose else 2

    if not found_urls["forms"] and not found_urls["queries"]:
        yield("No vulnerable forms or query parameters found.\n Trying default crawl...")
        await bot_detection_avoider(input_url, queue)
        
        while not queue.empty():
            yield await queue.get()
        
        manual_command += " --crawl=10 "
        async for result in run_sqlmap(input_url, "--form", "", level, 
                                       risk, threads, "", "", "", 
                                       flush_session, verbosity, manual_command):
            yield result
        return

    yield(f"Detected Form URLs: {found_urls['forms']}")
    yield(f"Detected Query URLs: {found_urls['queries']}")

    # Process forms
    for form_url in found_urls["forms"]:
        if injection_found:
            break
        await bot_detection_avoider(form_url, queue)
        
        while not queue.empty():
            yield await queue.get()
        
        async for result in run_sqlmap(form_url, "--form", "--smart", level, 
                                       risk, threads, "", "", "", 
                                       timeout, flush_session, verbosity, manual_command):
            yield result

    # Process query params
    for query_url in found_urls["queries"]:
        if injection_found:
            break
        await bot_detection_avoider(query_url, queue)
        
        while not queue.empty():
            yield await queue.get()
        
        async for result in run_sqlmap(query_url, "", "", level, 
                                       risk, threads, "", "", "", 
                                       timeout, flush_session, verbosity, manual_command):
            yield result

    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)

    if injection_log:
        injection_log = simplify_payload(injection_log)

        if detected_info: injection_log.append(f"\n=== Extracted Server Information ===\n")
        if detected_info["WEB_SERVER"]: injection_log.append(f"Web Server OS: {detected_info['WEB_SERVER']}")
        if detected_info["TECHNOLOGY"]: injection_log.append(f"Web App Tech: {detected_info['TECHNOLOGY']}")
        if detected_info["DBMS"]: injection_log.append(f"DBMS Type: {detected_info['DBMS']}")
        injection_log.append(f"\nTotal scan time: {minutes} minutes {seconds} seconds.")

        for log in injection_log:
            yield log
    else:
        yield "\nNo Vulnerabilities detected."


async def run_sqlmap(url, form, smart, level=5, risk=3, threads=10, referer="", cookie="",
                     csrf="", timeout=10, flush_session=True, verbosity=2, manual_command="", manual=False):
    global injection_found
    if injection_found:
        return

    manual = "" if manual else "--batch"
    cookie = f'--cookie="{cookie}"' if cookie else ""
    csrf = f'--csrf-token={csrf}' if csrf else ""
    flush_session = "--flush-session" if flush_session else ""
    referer = referer or url

    python_unbuffered = "set PYTHONUNBUFFERED=1 &&" if os.name == 'nt' else "PYTHONUNBUFFERED=1"

    command = f"{python_unbuffered} sqlmap {flush_session} -u \"{url}\" {manual} {form} \
            --level={level} --risk={risk} --threads={threads} {smart} \
            -v {verbosity} --random-agent --headers=\"Referer: {referer}; \
            Accept-Language: en-US,en;q=0.9\" {cookie} {csrf} \
            -o {manual_command}"

    yield f"Running SQLMap on: {url}\n"

    capturing = False
    second_hyphens = False
    suppress_output = False

    process = await asyncio.create_subprocess_shell(
        command, shell=True, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT
    )

    async for line in process.stdout:
        line = line.decode().strip()

        if "___" in line:
            suppress_output = True
            continue
        if any(keyword in line for keyword in ["[*]", "[PAYLOAD]", "[INFO]", "[DEBUG]", "[WARNING]"]):
            suppress_output = False
        if suppress_output:
            continue
        yield line

        if capturing:
            if "---" in line and not second_hyphens:
                injection_found = True
                second_hyphens = True
                injection_log.append(f"Exploitable URL: {url}\n")
            elif "---" in line and second_hyphens:
                capturing = False
            else:
                injection_log.append(line.strip())

        if any(keyword in line for keyword in ["identified the following injection", "resumed the following injection point(s)"]): 
            capturing = True

    await process.wait()
    yield f"\nScan for {url} completed."

def ensure_url_scheme(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        return f"http://{url}"
    return url
