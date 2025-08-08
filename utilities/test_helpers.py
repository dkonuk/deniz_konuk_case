import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestHelpers:
    """
    Utility class with helper methods for tests.
    """
    
    @staticmethod
    def take_screenshot(driver, test_name):
        """
        Take a screenshot and save it to a file.
        
        Args:
            driver: WebDriver instance
            test_name: Name of the test for the screenshot filename
            
        Returns:
            Path to the saved screenshot
        """
        # Create screenshots directory if it doesn't exist
        screenshots_dir = os.path.join(os.getcwd(), 'screenshots')
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        # Generate a unique filename with timestamp
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(screenshots_dir, filename)
        
        # Take the screenshot
        driver.save_screenshot(filepath)
        print(f"Screenshot saved to {filepath}")
        return filepath
    
    @staticmethod
    def wait_for_page_load(driver, timeout=10):
        """
        Wait for the page to fully load.
        
        Args:
            driver: WebDriver instance
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if page loaded within timeout, False otherwise
        """
        try:
            # Wait for the document.readyState to be 'complete'
            WebDriverWait(driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return True
        except TimeoutException:
            print(f"Page did not load completely within {timeout} seconds")
            return False
    
    @staticmethod
    def scroll_to_element(driver, element):
        """
        Scroll to make an element visible.
        
        Args:
            driver: WebDriver instance
            element: WebElement to scroll to
        """
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Add a small delay to allow the page to settle after scrolling
        time.sleep(0.5)
    
    @staticmethod
    def highlight_element(driver, element, duration=2):
        """
        Highlight an element on the page for debugging purposes.
        
        Args:
            driver: WebDriver instance
            element: WebElement to highlight
            duration: How long to highlight the element in seconds
        """
        # Store original style
        original_style = element.get_attribute("style")
        
        # Apply highlight style
        driver.execute_script(
            "arguments[0].setAttribute('style', 'border: 2px solid red; background: yellow;');",
            element
        )
        
        # Wait for the specified duration
        time.sleep(duration)
        
        # Restore original style
        driver.execute_script(
            f"arguments[0].setAttribute('style', '{original_style}');",
            element
        )
    
    @staticmethod
    def clear_cookies(driver):
        """
        Clear all cookies from the browser.
        
        Args:
            driver: WebDriver instance
        """
        driver.delete_all_cookies()
        print("All cookies cleared")
    
    @staticmethod
    def refresh_page(driver):
        """
        Refresh the current page.
        
        Args:
            driver: WebDriver instance
        """
        driver.refresh()
        TestHelpers.wait_for_page_load(driver)