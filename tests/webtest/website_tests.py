#!/usr/bin/env python3
import unittest
import os
import tracemalloc
import requests
from subprocess import check_output
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By



# Trace memory allocations in case if a file is not closed
# tracemalloc will close it for us!
tracemalloc.start()

class BasicTest(unittest.TestCase):
    
    def setUp(self):
        # Get the LAN ip from the system hostname command
        # strip it of it's newline and split the ip addresses
        # The first IP address will be the one we need, the others are gateways
        local_ip = check_output(['hostname', '--all-ip-addresses']).decode().strip().split(" ")[0]

        self.WEBSITE_URL = "http://{}:8080/".format(local_ip)


        self.driver = webdriver.Remote(
           desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
           command_executor=f"http://selenium_firefox:4444/wd/hub"
        )

        # Waits for the driver to be setup.
        self.driver.implicitly_wait(20)

    # Test som kollar om hemsidan innehåller en
    # <h1 class="title"> med texten "Välkommen till Floristgården!"
    def test_text_exist(self):
        validText = "Välkommen till Floristgården"
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        elem = driver.find_element(By.CLASS_NAME, "display-4")
        print("Checking if text exist and is correct...")
        self.assertEqual(elem.text, validText)


    # Test som kollar om hemsidans title innehåller "Floristgården"This is a modified jumbotron that occupies the entire horizontal space of its parent.
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


class InformationTest(unittest.TestCase):
    
    def setUp(self):
        # Get the LAN ip from the system hostname command
        # strip it of it's newline and split the ip addresses
        # The first IP address will be the one we need, the others are gateways
        local_ip = check_output(['hostname', '--all-ip-addresses']).decode().strip().split(" ")[0]

        self.WEBSITE_URL = "http://{}:8080/".format(local_ip)


        self.driver = webdriver.Remote(
           desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
           command_executor=f"http://selenium_firefox:4444/wd/hub"
        )

        # Waits for the driver to be setup.
        self.driver.implicitly_wait(20)
    
    # Tests if website contains address information
    def test_address_found(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        address = "Fjällgatan 32H 981 39 KIRUNA"
        
        print("Checking if address is found on website...")
        
        try:
            driver.find_element(By.PARTIAL_LINK_TEXT, address)
        except NoSuchElementException:
            self.fail("No address found")


    # Tests if website contains opening hours
    def test_opening_hours_found(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        open_hours = ['Måndagar 10-16', 'Tisdagar 10-16', 'Onsdagar 10-16', 'Torsdagar 10-16', 'Fredagar 10-16', 'Lördagar 12-15']

        opening_hours_elems = driver.find_elements(By.CLASS_NAME, "opening-hour")
        print(opening_hours_elems)
        for open_hour, index in opening_hours_elems:
            self.assertEqual(open_hour.text, open_hours[index])


    # Tests if website contains email and phonenumber
    def test_email_and_phonenumber_found(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        email = "info@DOMÄN"
        phonenumber = "0630-555-555"

        print("Checking if email is found on website...")

        try:
            driver.find_element(By.PARTIAL_LINK_TEXT, email)
        except NoSuchElementException:
            self.fail("No email found")

        print("Checking if phonenumber is found on website...")

        try:
            driver.find_element(By.PARTIAL_LINK_TEXT, phonenumber)
        except NoSuchElementException:
            self.fail("No phonenumber found")        


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
