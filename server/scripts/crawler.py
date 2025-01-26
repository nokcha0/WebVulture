import requests
from bs4 import BeautifulSoup

queue = None

async def init_queue(q):
    global queue
    queue = q

async def crawler(base_url, max_depth=10):
    if queue is None:
        raise ValueError("Queue has not been initialized. Call init_queue first.")

    visited_urls = set()
    urls_to_crawl = {base_url}
    found_urls = {"forms": set(), "queries": set(), "all_links": set()}
    depth = 0

    while urls_to_crawl and depth < max_depth:
        url = urls_to_crawl.pop()
        if url in visited_urls:
            continue
        visited_urls.add(url)

        try:
            await queue.put(f"Crawling: {url}")
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                found_urls["all_links"].add(url)
                for link in soup.find_all('a', href=True):
                    full_url = requests.compat.urljoin(base_url, link['href'])
                    found_urls["all_links"].add(full_url)
                    await queue.put(f"Found URL: {full_url}")

        except requests.RequestException as e:
            await queue.put(f"Error crawling {url}: {e}")

        depth += 1

    await queue.put("Crawling finished.")
    return {
        "forms": list(found_urls["forms"]),
        "queries": list(found_urls["queries"])
    }

query_kw = [
    "?id=",
    "?user=",
    "?product=",
    "?category=",
    "?query=",
    "?page=",
    "?article=",
    "?pid=",
    "?uid=",
    "?name=",
    "?search=",
    "?keyword=",
    "?type=",
    "?item=",
    "?order=",
    "?lang=",
    "?ref=",
    "?view=",
    "?action=",
    "?module=",
    "?dir=",
    "?folder=",
    "?path=",
    "?file=",
    "?doc=",
    "?blog=",
    "?post=",
    "?show=",
    "?news=",
    "?cmd=",
    "?exec=",
    "?download=",
    "?email=",
    "?comment=",
    "?feedback="
]

form_kw = [
    "user",
    "login",
    "auth",
    "signin",
    "signup",
    "register",
    "account",
    "username",
    "email",
    "password",
    "passwd",
    "pwd",
    "pass",
    "admin",
    "secure",
    "session",
    "token",
    "csrf",
    "verify",
    "confirm",
    "reset",
    "recover",
    "forgot",
    "profile",
    "contact",
    "message",
    "post",
    "submit"
]

