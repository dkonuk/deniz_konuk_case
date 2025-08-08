from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from config import Config

class CareersPage(BasePage):

    teams_block = (By.CSS_SELECTOR, "#career-find-our-calling")
    locations_block = (By.CSS_SELECTOR, "[data-id='38b8000']")
    life_at_insider_block = (By.CSS_SELECTOR, "[data-id='c06d1ec']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def check_if_teams_block_loaded(self):
        try:
            self.check_if_element_is_visible(self.teams_block)
            return True
        except:
            return False

    def check_if_locations_block_loaded(self):
        try:
            self.check_if_element_is_visible(self.locations_block)
            return True
        except:
            return False

    def check_if_life_at_insider_block_loaded(self):
        try:
            self.check_if_element_is_visible(self.life_at_insider_block)
            return True
        except:
            return False