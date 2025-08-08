from pages.home_page import HomePage


class TestHomePage:

    def test_homepage_to_careers_navigation(self, fixtureSetup):
        # HomePage actions
        driver = fixtureSetup
        home_page = HomePage(driver)
        home_page.accept_cookies_if_present()
        assert home_page.check_if_the_page_loaded(), "Homepage did not load successfully - navigation bar not found"
        home_page.click_company_link()
        #Careers Page actions
        careers_page = home_page.click_careers_link()
        assert careers_page.check_if_teams_block_loaded(), "Teams block not found on Careers page"
        assert careers_page.check_if_locations_block_loaded(), "Careers block not found on Careers page"
        assert careers_page.check_if_life_at_insider_block_loaded(), "Life at Insider block not found on Careers page"



