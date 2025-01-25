import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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


def crawler(base_url, max_depth=10):

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
            print(f"Crawling: {url}")
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                found_urls["all_links"].add(url)
                for link in soup.find_all('a', href=True):
                    if link['href'].lower():
                        url = requests.compat.urljoin(base_url, link['href'])
                        found_urls["all_links"].add(url)
                        print(f"Found URL: {url}")
                        
        except requests.RequestException as e:
            print(f"Error crawling {url}: {e}")

        depth += 1

    for link in found_urls["all_links"]:
        # query
        if any(keyword in link.lower() for keyword in query_kw):
            found_urls["queries"].add(link)
            print(f"URL with potential query injection: {link}")

        # form
        if any(keyword in link.lower() for keyword in form_kw):
            found_urls["forms"].add(link)
            print(f"URL with potential form injection: {link}")


    return {
        "forms": list(found_urls["forms"]),
        "queries": list(found_urls["queries"])
    }
