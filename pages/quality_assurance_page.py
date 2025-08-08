from pages.base_page import BasePage
from pages.open_positions_page import OpenPositionsPage
from selenium.webdriver.common.by import By
from config import Config


class QualityAssurancePage(BasePage):
    see_all_qa_jobs_button = (By.CSS_SELECTOR, "a[href='https://useinsider.com/careers/open-positions/?department=qualityassurance']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.BASE_URL + "careers/quality-assurance/")

    def click_see_all_qa_jobs_button(self):
        self.click_element(self.see_all_qa_jobs_button)
        return OpenPositionsPage(self.driver)



