#!/usr/bin/env python3
import unittest
import os
import tracemalloc
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#!!!! TESTAR TEMPORÄRT NTI FÖR ATT FÖRSTÅ SELENIUM MED CI!!!!!!
WEBSITE_URL = "https://www.ntigymnasiet.se/uppsala/"

tracemalloc.start()

class WebsiteTest(unittest.TestCase):
    
    def setUp(self):
        global WEBSITE_URL
        self.WEBSITE_URL = WEBSITE_URL

        self.username = "elias.juremalm@elev.ga.ntig.se"
        self.authkey = "u84bc8cf893b9973"

        caps = {}
        caps['browserName'] = 'Firefox'
        caps['version'] = 'Latest'
        caps['platform'] = 'Headless'
        caps['screenResolution'] = '1920x1080'

        self.driver = webdriver.Remote(
           desired_capabilities=caps,
           command_executor=f"http://{self.username}:{self.authkey}@hub-cloud.crossbrowsertesting.com:80/wd/hub"
        )

        self.driver.implicitly_wait(20)


    # Test som kollar om hemsidan innehåller en
    # <h1 class="title"> med texten "Välkommen till Floristgården!"
    def test_text_exist(self):
        validText = "ALLA ÄR MED OCH UTVECKLAS"
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        elem = driver.find_element_by_class_name('title-xl')
        print("Checking if text exist and is correct...")
        self.assertEqual(elem.text, validText)


    # Test som kollar om hemsidans title innehåller "Floristgården"
    def test_title_exist(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        validTitle = "NTI"
        print("Checking if title is correct.")
        self.assertIn(validTitle, driver.title) 
    

    # Test som kollar ifall hemsidan är fungerande och 
    # tillgänglig från internet.
    def test_website_up_and_running(self):
        response = requests.get(self.WEBSITE_URL)
        print("Checking if website is up and running on the big web!")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
