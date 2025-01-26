## Inspiration
Current SQL injection tools, such as sqlmap, are CLI-based and require technical expertise, including integration with tools like Burp Suite. They are not so intuitive and require manual separation of forms and queries, making pentesting less accessible. WEBVULTURE addresses these challenges with enhanced features and a user-friendly approach, offering automated crawling, bot detection avoidance, and comprehensive attack surface identification to streamline the process and minimize manual effort.

## What it does
Given a URL, WEBVULTURE crawls the website, identifies potential SQL injection points in queries and form inputs, mimics human-like interactions using Selenium to bypass bot detection, and brute-forces SQLi payloads to assess security vulnerabilities.

tl;dr: you give it a URL, and it tries to hack its databases!

## How we built it
Frontend: React (JS) and Vite
Backend: Python w/ fastAPI
Selenium, sqlmap, beautifulsoup.

## Challenges we ran into
- Mimicking human interaction and avoiding bot detection
- Asynchronous communication from backend to frontend using Server-Sent Events (SSE)

## Accomplishments that we're proud of
- Successful website crawling with injectable form and query detection
- Selenium-based bot detection avoider
- Real-time display of terminal outputs of backend scripts in frontend

## What we learned
- Workflow for frontend and backend collaboration
- Writing tests and debugging API requests

## What's next for WEBVULTURE.
- More features, attack methods (ex: XSS, CSRF, SSRF...), and customizability: the end goal is for everyone to be able to test the safety of their website with just a few clicks.

## Disclaimer
This website is intended for educational and research purposes only. SQL injection may only be used on websites that you own or have explicit permission to test. Unauthorized use is punishable by law as described in section 342.1 of the Canadian Criminal Code, which may result in imprisonment for up to 10 years. By using this site, you agree that the owners and contributors of this site are not liable for any misuse or damage resulting from the information or tools provided.