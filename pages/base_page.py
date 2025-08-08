from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from config import Config
import time


class BasePage:
    cookies_dialogue = (By.CSS_SELECTOR, ".cli-bar-btn_container")
    accept_cookies = (By.CSS_SELECTOR, "[data-cli_action='accept_all']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)
        self.driver.get(Config.BASE_URL)

    def accept_cookies_if_present(self):
        try:
            self.find_element(self.cookies_dialogue)
            self.click_element(self.accept_cookies)
            print("Cookies accepted")
        except:
            pass # Cookie dialog is not present or not clickable

    def find_element(self, element_locator):
        return self.wait.until(EC.presence_of_element_located(element_locator))

    def click(self, element_locator):
        self.click_element(element_locator)

    def check_if_element_is_visible(self, element_locator):
        return self.wait.until(EC.visibility_of_element_located(element_locator))

    def find_clickable_element(self, element_locator):
        return self.wait.until(EC.element_to_be_clickable(element_locator))

    def click_element(self, element_locator):
        element = self.find_clickable_element(element_locator)
        element.click()

    def get_text_from_element(self, element_locator):
        element_to_get_text = self.find_element(element_locator)
        return element_to_get_text.text

    def scroll_to_element(self, element_locator):
        element = self.find_element(element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(0.5)

    def find_elements(self, *element_locator):
        return self.wait.until(EC.visibility_of_element_located(*element_locator))

    def hover_and_click(self, parent_element, child_locator):
        actions = ActionChains(self.driver)
        parent_locator = self.find_element(parent_element)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",parent_locator)
        time.sleep(1)

        actions.move_to_element(parent_locator).perform()
        child = parent_locator.find_element(*child_locator)
        child.click()


    def click_and_select_from_dropdown(self, dropdown_menu_locator, dropdown_option, filtering_option):
        # dropdown_menu_locator : Locator for the dropdown menu to be selected
        # dropdown_option : Visible text of option to be selected from the dropdown menu
        # filterin_option : What is the dropdown menu used to filter (Location, department etc.)
        # Open dropdown with JavaScript
        self.driver.execute_script(f"document.querySelector('{dropdown_menu_locator}').click();")

        # Wait a moment for dropdown to render
        time.sleep(1)
        # Use Select2 API to set the value directly
        self.driver.execute_script(f"""
                $('#filter-by-{filtering_option}').val('{dropdown_option}').trigger('change');
            """)

