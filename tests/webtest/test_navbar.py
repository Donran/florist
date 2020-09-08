import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class NavbarTest(WebTestBase.BaseTest):
    def test_navbar(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        required_links = [
            "Hem",
            "Personal",
            "Hitta Hit"
        ]
        navbar_items = driver.find_elements(By.CLASS_NAME, "nav-item")
        found = 0
        for item in navbar_items:
            link = item.find_element(By.CLASS_NAME, "nav-link")
            href = link.get_attribute("href") ## make sure all links are visitable
            name = link.text
            if name in required_links:
                found += 1

        self.assertGreaterEqual(len(required_links), found)
