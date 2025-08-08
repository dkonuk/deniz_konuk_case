from selenium.common import TimeoutException
import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config

class OpenPositionsPage(BasePage):
    filter_by_location_dropdown = '#select2-filter-by-location-container'
    istanbul_location_selector = (By.CSS_SELECTOR, "li[id*='Istanbul, Turkiye']")
    dropdown_menu_filter_option = "location"
    item_to_be_selected_from_filter_by_location_dropdown = "Istanbul, Turkiye"
    jobs_listing =  (By.CSS_SELECTOR, "#jobs-list")
    view_role_button = (By.CSS_SELECTOR, "a.btn.btn-navy")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    def wait_for_department_selection_to_show_quality_assurance(self, timeout=10):
        """Wait for the department dropdown to show 'Quality Assurance' selection"""
        try:
            element = self.wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.ID, "select2-filter-by-department-container"),
                    "title",
                    "Quality Assurance"
                )
            )
        except TimeoutException:
            raise AssertionError(f"Department dropdown did not show 'Quality Assurance' within {timeout} seconds")


    def select_istanbul_location_with_javascript_click(self):
        self.click_and_select_from_dropdown(self.filter_by_location_dropdown, self.item_to_be_selected_from_filter_by_location_dropdown, self.dropdown_menu_filter_option)

    def check_if_there_jobs_available(self):
        parent_element = self.find_element(self.jobs_listing)
        direct_children = parent_element.find_elements(By.XPATH, "./*")
        if len(direct_children) > 0:
            return True
        else:
            return False

    def get_job_listings_text(self):
        parent_element = self.check_if_element_is_visible(self.jobs_listing)
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.position-list-item")))
        # Get all job cards inside the container
        job_cards = parent_element.find_elements(By.CSS_SELECTOR, "div.position-list-item")
        time.sleep(2)
        self.scroll_to_element(self.jobs_listing)
        time.sleep(1)
        # Refreshing elements in case they became stale
        parent_element = self.find_element(self.jobs_listing)
        job_cards = parent_element.find_elements(By.CSS_SELECTOR, "div.position-list-item")
        jobs_data = []
        # Loop and extract details
        for card in job_cards:
            title = card.find_element(By.CSS_SELECTOR, ".position-title").text
            dept = card.find_element(By.CSS_SELECTOR, ".position-department").text
            location = card.find_element(By.CSS_SELECTOR, ".position-location").text

            jobs_data.append({
                "title": title,
                "department": dept,
                "location": location
            })
        return jobs_data

    def click_view_role_button_and_check_redirect(self):
        original_window = self.driver.current_window_handle
        current_window_count = len(self.driver.window_handles)
        self.hover_and_click(self.jobs_listing, self.view_role_button)
        self.wait.until(lambda d: len(d.window_handles) > current_window_count)
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        self.wait.until(EC.url_contains("jobs.lever.co"))
        current_url = self.driver.current_url
        return current_url




