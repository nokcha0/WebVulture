# Inspiration
Current SQL injection tools (i.e., SQLMap) can only target one specific endpoint at a time, making it inconvenient for pentesting real-world web apps which contain dozens of pages. This problem will be solved by WEBVULTURE, which will have the ability to crawl the entire app and find all possible attack points.

# What it does
Given a URL, WEBVULTURE crawls the website, identifies potential SQL injection points in queries and form inputs, mimics human-like interactions using Selenium to bypass bot detection, and brute-forces SQLi payloads to assess security vulnerabilities.

**tl;dr:** you give it a URL, and it tries to hack its databases!

# How we built it
- **Frontend:** React (JS) and Vite
- **Backend:** Python w/ FastAPI
- Selenium, SQLMap

# Challenges we ran into
- Asynchronous file transfer in backend using server-sent events
- Asynchronous communication from backend to frontend

# Accomplishments that we're proud of
- Successful website crawling with injectable form and query detection
- Selenium-based bot detection avoider
- Real-time display of terminal outputs of backend scripts in frontend

# What's next for WEBVULTURE
More features, attack methods, customizability: the end goal is for everyone to be able to test the safety of their website with just a few clicks of their mouse.