from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_terms_and_conditions_window_handling():
    # Set up BrowserStack credentials
    USERNAME = "kinjalpatel_OYWK3u"  # Replace with your BrowserStack username
    ACCESS_KEY = "cequyzAGshrun9nyoz9f"  # Replace with your BrowserStack access key

    # Desired capabilities for BrowserStack (using Chrome on Windows 10, for example)
    desired_cap = {
        'os': 'Windows',
        'os_version': '11',
        'browser': 'Chrome',
        'browser_version': 'latest',
        'name': 'BrowserStack Test',  # Name of the test on BrowserStack
        'build': 'Build 1',           # Optional: Name of the build
        'browserstack.local': 'false',
        'browserstack.selenium_version': '4.0.0'
    }

    # Set up WebDriver for BrowserStack
    driver = webdriver.Remote(
        command_executor=f'https://{"kinjalpatel_OYWK3uE}:{cequyzAGshrun9nyoz9f}@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap
    )

    # Step 1: Navigate to Target sign-in page
    driver.get("https://www.target.com/login")

    # Maximize window for visibility
    driver.maximize_window()

    # Step 2: Click on the 'Terms and Conditions' link
    terms_link = driver.find_element(By.LINK_TEXT, "Target terms and conditions")
    terms_link.click()

    # Step 3: Get the current window handle (for switching back later)
    original_window = driver.current_window_handle

    # Step 4: Switch to the newly opened window
    # Wait for new windows to open
    time.sleep(10)
    all_windows = driver.window_handles
    for window in all_windows:
        if window != original_window:
            driver.switch_to.window(window)
            break

    # Step 5: Verify the Terms and Conditions page has opened by checking the page title or URL
    assert "terms" in driver.title.lower() or "terms" in driver.current_url, "Terms and Conditions page did not open."

    # Close the newly opened window
    driver.close()

    # Step 6: Switch back to the original window
    driver.switch_to.window(original_window)

    # Optionally, verify you're back on the sign-in page
    assert "login" in driver.current_url, "Failed to switch back to the original window."

    # Quit the browser session
    driver.quit()

# Call the test function
test_terms_and_conditions_window_handling()
