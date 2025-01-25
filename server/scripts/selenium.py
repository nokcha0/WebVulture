import sys
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import WebDriverException, TimeoutException

def bot_detection_avoider(url):
    try:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")  # Run headless
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
        chrome_options.add_argument("--allow-running-insecure-content")  # Allow mixed content
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection

        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get(url)
        except TimeoutException:
            print(f"Error: The URL '{url}' took too long to respond.")
            driver.quit()
            sys.exit(1)
        except WebDriverException:
            print(f"Error: The URL '{url}' is invalid or not accessible.")
            driver.quit()
            sys.exit(1)

        # Get referer
        referer = str(driver.execute_script("return document.referrer;"))
        if not referer:
            print("Referer could not be obtained, using the provided URL.")
            referer = url
        else:
            print("Referer obtained:", referer)

        # Get cookies
        cookies = driver.get_cookies()
        cookie = "; ".join([f"{c['name']}={c['value']}" for c in cookies])

        if cookie:
            print("Cookies obtained:", cookie)
        else:
            print("No cookies found.")

        # Extract CSRF token
        csrf = driver.execute_script("""
            return document.querySelector('input[name="csrf_token"], meta[name="csrf-token"]')?.getAttribute('content');
        """) or ""

        if csrf:
            print("CSRF Token obtained:", csrf)
        else:
            print("CSRF Token could not be obtained.")

        driver.quit()
        return referer, cookie, csrf

    except WebDriverException as e:
        print(f"WebDriver error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
