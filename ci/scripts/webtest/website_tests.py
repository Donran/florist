#!/usr/bin/env python3
import unittest
import os
import tracemalloc
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


local_ip = __import__("subprocess").check_output(['hostname', '--all-ip-addresses']).decode().strip().split(" ")[0]

#!!!! TESTAR TEMPORÄRT NTI FÖR ATT FÖRSTÅ SELENIUM MED CI!!!!!!
#WEBSITE_URL = "https://www.ntigymnasiet.se/uppsala/"
WEBSITE_URL = "http://{}:8080/".format(local_ip)

tracemalloc.start()

class WebsiteTest(unittest.TestCase):
    
    def setUp(self):
        global WEBSITE_URL
        self.WEBSITE_URL = WEBSITE_URL


        self.driver = webdriver.Remote(
           desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
           command_executor=f"http://selenium_firefox:4444/wd/hub"
        )

        self.driver.implicitly_wait(20)


    # Test som kollar om hemsidan innehåller en
    # <h1 class="title"> med texten "Välkommen till Floristgården!"
    def test_text_exist(self):
        validText = "Välkommen till Floristgården!"
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        elem = driver.find_element(By.CLASS_NAME, "title")
        print("Checking if text exist and is correct...")
        self.assertEqual(elem.text, validText)


    # Test som kollar om hemsidans title innehåller "Floristgården"
    def test_title_exist(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        validTitle = "Floristgården"
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
    print("hostname: "+local_ip)
    unittest.main()
