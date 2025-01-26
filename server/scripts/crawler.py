import aiohttp
import asyncio
from urllib.parse import urljoin  # Correct import
from bs4 import BeautifulSoup

queue = None  # Global queue variable

async def init_queue(q):
    """Initialize the queue for async communication."""
    global queue
    queue = q

async def crawler(base_url, max_depth=10):
    if queue is None:
        raise ValueError("Queue has not been initialized. Call init_queue first.")

    visited_urls = set()
    urls_to_crawl = {base_url}
    found_urls = {"forms": set(), "queries": set(), "all_links": set()}
    depth = 0

    async with aiohttp.ClientSession() as session:
        while urls_to_crawl and depth < max_depth:
            url = urls_to_crawl.pop()
            if url in visited_urls:
                continue
            visited_urls.add(url)

            try:
                await queue.put(f"Crawling: {url}")
                async with session.get(url) as response:
                    if response.status == 200:
                        text = await response.text()
                        soup = BeautifulSoup(text, 'html.parser')
                        found_urls["all_links"].add(url)
                        for link in soup.find_all('a', href=True):
                            if link['href'].lower():
                                full_url = urljoin(base_url, link['href'])  # Corrected usage
                                found_urls["all_links"].add(full_url)
                                await queue.put(f"Found URL: {full_url}")

            except aiohttp.ClientError as e:
                await queue.put(f"Error crawling {url}: {e}")

            depth += 1

    for link in found_urls["all_links"]:
        if any(keyword in link.lower() for keyword in query_kw):
            found_urls["queries"].add(link)
            await queue.put(f"URL with potential query injection: {link}")

        if any(keyword in link.lower() for keyword in form_kw):
            found_urls["forms"].add(link)
            await queue.put(f"URL with potential form injection: {link}")

    await queue.put("Crawling finished.")
    return {
        "forms": list(found_urls["forms"]),
        "queries": list(found_urls["queries"])
    }

query_kw = [
    "?id=", "?user=", "?product=", "?category=", "?query=", "?page=", "?article=",
    "?pid=", "?uid=", "?name=", "?search=", "?keyword=", "?type=", "?item=", "?order=",
    "?lang=", "?ref=", "?view=", "?action=", "?module=", "?dir=", "?folder=", "?path=",
    "?file=", "?doc=", "?blog=", "?post=", "?show=", "?news=", "?cmd=", "?exec=",
    "?download=", "?email=", "?comment=", "?feedback="
]

form_kw = [
    "user", "login", "auth", "signin", "signup", "register", "account",
    "username", "email", "password", "passwd", "pwd", "pass", "admin",
    "secure", "session", "token", "csrf", "verify", "confirm", "reset",
    "recover", "forgot", "profile", "contact", "message", "post", "submit"
]
