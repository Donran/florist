import WebTestBase
import requests
from selenium.webdriver.common.by import By

class SocialMediaTest(WebTestBase.BaseTest):


    # Tests if the website contains the social 
    # media icons
    def test_socialmedia_icons(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        icons = driver.find_elements(By.CLASS_NAME, "fab")
        found = 0

        for item in icons:
            found += 1

        self.assertEqual(found, 3)

    # Tests if the icon links work and direct
    # the user to the correct website
    def test_socialmedia_links(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        required_links = [
            "https://facebook.com/ntiuppsala/",
            "https://twitter.com/ntiuppsala",
            "https://www.instagram.com/ntiuppsala/"
        ]
        links = driver.find_elements(By.CLASS_NAME, "social-link")
        found = 0
        for item in links:
            href = item.get_attribute("href") ## Gets the link 
            if href not in required_links:
                self.fail("Could not find required link: {}".format(href))
            r = requests.get(href)
            if r.status_code == 404:
                self.fail("Could not establish a connection with link: {}".format(href))
            else:
                found += 1

        self.assertEqual(len(required_links), found)
