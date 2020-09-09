import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestMap(WebTestBase.BaseTest):
    # Test to make sure map is present on hitta_hit
    def test_products(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"/hitta_hit.html")

        try:
            driver.find_element(By.ID, "map")
        except NoSuchElementException:
            self.fail("No map found.")