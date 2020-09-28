import WebTestBase
import requests
from os import path
from selenium.webdriver.common.by import By
class NavbarTest(WebTestBase.BaseTest):
    def test_navbar(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        required_links = {
            "Hem": "index.html",
            "Personal": "personal.html",
            "Hitta hit": "hitta_hit.html"
        }
        navbar_items = driver.find_elements(By.CLASS_NAME, "nav-item")
        found = 0
        for item in navbar_items:
            link = item.find_element(By.CLASS_NAME, "nav-link")
            href = link.get_attribute("href") ## make sure all links are visitable
            name = link.text
            file_name = path.basename(href)
            if file_name not in required_links.values():
                self.fail("Could not find required link: {}".format(file_name))
            r = requests.get(href)
            if r.status_code == 404:
                self.fail("Could not find link: {}".format(href))
            if name in required_links:
                found += 1
        self.assertGreaterEqual(len(required_links), found)

