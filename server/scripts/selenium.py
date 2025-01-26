import asyncio
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import WebDriverException, TimeoutException

async def bot_detection_avoider(url, queue):
    try:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get(url)
        except TimeoutException:
            await queue.put({"error": f"Error: The URL '{url}' took too long to respond."})
            driver.quit()
            return
        except WebDriverException:
            await queue.put({"error": f"Error: The URL '{url}' is invalid or not accessible."})
            driver.quit()
            return

        referer = str(driver.execute_script("return document.referrer;")) or url
        await queue.put({"message": f"Referer obtained: {referer}"})

        cookies = driver.get_cookies()
        cookie = "; ".join([f"{c['name']}={c['value']}" for c in cookies]) or "No cookies found."
        await queue.put({"message": f"Cookies obtained: {cookie}"})

        csrf = driver.execute_script("""return document.querySelector('input[name="csrf_token"], meta[name="csrf-token"]')?.getAttribute('content');""") or "No CSRF token found."
        await queue.put({"message": f"CSRF Token obtained: {csrf}"})

        driver.quit()
        await queue.put({"result": (referer, cookie, csrf)})

    except WebDriverException as e:
        await queue.put({"error": f"WebDriver error: {e}"})
    except Exception as e:
        await queue.put({"error": f"An unexpected error occurred: {e}"})
