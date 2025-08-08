from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.careersPage import CareersPage
from config import Config


class HomePage(BasePage):

    navigationbar = (By.CSS_SELECTOR, '#navbarNavDropdown')
    navigationbar_company = (By.XPATH, "//a[contains(text(), 'Company')]")
    navigationbar_company_careers = (By.XPATH, "//a[text()='Careers']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.BASE_URL)

    def check_if_the_page_loaded(self):
        try:
            self.find_element(self.navigationbar)
            return True
        except TimeoutException:
            return False

    def click_company_link(self):
        self.click_element(self.navigationbar_company)

    def click_careers_link(self):
        self.click_element(self.navigationbar_company_careers)
        return CareersPage(self.driver)
