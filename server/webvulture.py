import subprocess, time, os
from urllib.parse import urlparse
from scripts.crawler import *
from scripts.selenium import *

injection_found = False
injection_log = []
start_time = 0
detected_info = {"WEB_SERVER": None, "TECHNOLOGY": None, "DBMS": None}

def core():
    global start_time
    try:
        input_url = input("Enter Target URL: ").strip()
        strength = 3
        threads = 10
        timeout = 10 # Lower -> Fast, less accurate. Higher -> Slow, more accurate
        flush_session = True
        manual_command = input("Enter manual command: ")

        if strength not in range(1, 6) or threads not in range(1, 11):
            print("Invalid input values")
            return

        input_url = ensure_url_scheme(input_url) 

        # Strength Mapping:
        # Attack Strength | Level | Risk
        # 1: 1 , 1 | Basic Scanning, Minimal Payloads
        # 2: 2 , 2 | Slightly more aggressive scanning
        # 3: 3 , 3 | Balanced Intrusion
        # 4: 4 , 3 | Aggressive Intrusion
        # 5: 5 , 3 | Maximum strength, high risk

        if strength == 1:
            level, risk = 1, 1
        elif strength == 2:
            level, risk = 2, 2
        elif strength == 3:
            level, risk = 3, 3
        elif strength == 4:
            level, risk = 4, 3
        elif strength == 5:
            level, risk = 5, 3 

        print(f"URL given: {input_url}")
        start_time = time.time() 
        process_targets(input_url, level, risk, threads, timeout, flush_session, manual_command)

    except ValueError:
        print("Invalid input")

def process_targets(input_url, level, risk, threads, timeout, flush_session, manual_command):
    global injection_found
    global start_time

    print(f"\nCrawling and analyzing {input_url} for vulnerabilities...")
    found_urls = crawler(input_url)

    if not found_urls["forms"] and not found_urls["queries"]:
        print("No vulnerable forms or query parameters found.\n Trying default crawl...")
        referer, cookie, csrf = bot_detection_avoider(input_url)
        manual_command += " --crawl=10 "
        run_sqlmap(input_url, "--form", "--smart", level, 
                   risk, threads, referer, cookie, csrf, 
                   flush_session, manual_command)
        return

    print(f"Detected Form URLs: {found_urls['forms']}")
    print(f"Detected Query URLs: {found_urls['queries']}")

    # form
    for form_url in found_urls["forms"]:
        if injection_found:
            break 

        referer, cookie, csrf = bot_detection_avoider(form_url)
        run_sqlmap(form_url, "--form", "--smart", level, 
                   risk, threads, referer, cookie, csrf, 
                   timeout, flush_session, manual_command)
    
    # query 
    for query_url in found_urls["queries"]:
        if injection_found:
            break 

        referer, cookie, csrf = bot_detection_avoider(query_url)
        run_sqlmap(query_url, "", "", level, 
                   risk, threads, referer, cookie, csrf, 
                   timeout, flush_session, manual_command)

    end_time = time.time()  # End measuring time
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)

    if injection_log:

        if detected_info["WEB_SERVER"]: injection_log.append(f"Web Server OS: {detected_info["WEB_SERVER"]}")
        if detected_info["TECHNOLOGY"]: injection_log.append(f"Web App Tech: {detected_info["TECHNOLOGY"]}")
        if detected_info["DBMS"]: injection_log.append(f"DBMS Type: {detected_info["DBMS"]}")
        injection_log.append(f"Total scan time: {minutes} minutes {seconds} seconds.")

        print("\n==== Vulnerability Found ====\n")
        print("\n".join(injection_log))
        print("\n=============================\n")

    else:
        print("\nNo Vulnerabilities detected.")

def run_sqlmap(url, form, smart, level=5, risk=3, threads=10, referer="", cookie=""
               , csrf="", timeout=10, flush_session=True, manual_command="", manual=False, verbosity=2):
    global injection_found
    if injection_found:
        return
    
    manual = "" if manual else "--batch"
    cookie = f'--cookie="{cookie}"' if cookie else ""
    csrf = f'--csrf-token={csrf}' if csrf else ""
    flush_session = "--flush-session" if flush_session else ""
    referer = referer or url

    if os.name == 'nt':  # Windows
        pythonunbuffered = "set PYTHONUNBUFFERED=1 &&"
    else:  # Linux/Mac
        pythonunbuffered = "PYTHONUNBUFFERED=1"

    command = f"{pythonunbuffered} sqlmap {flush_session} -u \"{url}\" {manual} {form} \
            --level={level} --risk={risk} --threads={threads} {smart} \
            -v {verbosity} --random-agent --headers=\"Referer: {referer}; \
            Accept-Language: en-US,en;q=0.9\" {cookie} {csrf} \
            timeout={timeout} \
            {manual_command} "

    print(f"Running SQLMap on: {url}\n ")

    capturing = False
    second_hyphens = False
    suppress_output = False

    with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1) as process:
        for line in iter(process.stdout.readline, ''):
            if "___" in line:
                suppress_output = True
                continue
            if any(keyword in line for keyword in ["[*]", "[PAYLOAD]", "[INFO]", "[DEBUG]", "[WARNING]"]):
                suppress_output = False
            if  suppress_output: 
                continue
            print(line, end='', flush=True)  

            if capturing:
                if "---" in line and not second_hyphens:
                    injection_found = True
                    second_hyphens = True
                    injection_log.append(f"Exploitable URL: {url}\n")
                elif "---" in line and second_hyphens:
                    capturing = False
                else:
                    injection_log.append(line.strip())

            if "identified the following injection" in line:
                capturing = True

            if "web server operating system" in line:
                detected_info["WEB_SERVER"] = line.split(": ", 1)[1].strip() if ": " in line else line.strip()
            if "web application technology" in line:
                detected_info["TECHNOLOGY"] = line.split(": ", 1)[1].strip() if ": " in line else line.strip()
            if "back-end dbms" in line:
                detected_info["DBMS"] = line.split(": ", 1)[1].strip() if ": " in line else line.strip()

        process.stdout.close()
        process.wait()

    print(f"\nScan for {url} completed.")

def ensure_url_scheme(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        return f"http://{url}"
    return url

if __name__ == "__main__":
    core()

