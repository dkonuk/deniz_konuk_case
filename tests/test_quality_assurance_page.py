from pages.quality_assurance_page import QualityAssurancePage
import time


class TestQualityAssurancePage:
    def test_quality_assurance_page(self, fixtureSetup):
        quality_assurance_page = QualityAssurancePage(fixtureSetup)
        #Starting at the Careers/Quality Assurance Page
        quality_assurance_page.accept_cookies_if_present()
        open_positions_page = quality_assurance_page.click_see_all_qa_jobs_button()
        # Redirected to Careers/Open Positions Page
        open_positions_page.wait_for_department_selection_to_show_quality_assurance()
        open_positions_page.select_istanbul_location_with_javascript_click()
        #Waiting for relevant Job Postings to Load
        time.sleep(2)
        assert open_positions_page.check_if_there_jobs_available(), "There are no jobs available for Istanbul"
        jobs = open_positions_page.get_job_listings_text()
        #Checking if the listed job postings have the correct location, title and positions
        for job in jobs:
            department = job["department"]
            assert "Quality Assurance" in department, f"Expected 'Quality Assurance' to be in department, but got: '{department}'"

            location = job["location"]
            assert "Istanbul, Turkiye" in location, f"Expected 'Istanbul, Turkiye' to be in location, but got: '{location}'"

            title = job["title"]
            assert "Quality Assurance" in title, f"Expected 'Quality Assurance' to be in title, but got: '{title}'"
        url = open_positions_page.click_view_role_button_and_check_redirect()
        assert "jobs.lever.co" in url, "Redirect to Lever Page Failed"



