import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestHeaderButtons(WebTestBase.BaseTest):

    # Test to check if buttons exist in header.
    def test_buttons_exist(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"/index.html")

        try:
            driver.find_element(By.ID, "opening-hours-btn")
        except NoSuchElementException:
            self.fail("No opening hours button found.")

        try:
            driver.find_element(By.ID, "our-products-btn")
        except NoSuchElementException:
            self.fail("No our products button found.")