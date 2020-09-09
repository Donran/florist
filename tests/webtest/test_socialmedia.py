import WebTestBase
import requests
from selenium.webdriver.common.by import By

class SocialMediaTest(WebTestBase.BaseTest):

    # Tests if the website contains the social media icons 
    # that links to Floristgården's social medias
    def test_socialmedia(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        required_links = [
            "https://facebook.com/ntiuppsala/",
            "https://twitter.com/ntiuppsala",
            "https://www.instagram.com/ntiuppsala/"
        ]
        icons = driver.find_elements(By.CLASS_NAME, "social-link")
        found = 0
        for item in icons:
            href = item.get_attribute("href") ## Gets the link 
            if href not in required_links:
                self.fail("Could not find required link: {}".format(href))
            r = requests.get(href)
            if r.status_code == 404:
                self.fail("Could not establish a connection with link: {}".format(href))
            else:
                found += 1

        self.assertEqual(len(required_links), found)
