#!/usr/bin/env python3
import unittest
from subprocess import check_output
from selenium import webdriver

class BaseTest(unittest.TestCase):

    def setUp(self):
        # Get the LAN ip from the system hostname command
        # strip it of it's newline and split the ip addresses
        # The first IP address will be the one we need, the others are gateways
        # This is needed because we need to be able to give the standalone firefox service
        # the ip address of the container running this script.
        local_ip = check_output(['hostname', '--all-ip-addresses']).decode().strip().split(" ")[0]

        self.WEBSITE_URL = "http://{}:8080/".format(local_ip)

        # selenium_firefox is a hostname for the firefox standalone service, see: .gitlab-ci.yml
        self.driver = webdriver.Remote(
           desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
           command_executor=f"http://selenium_firefox:4444/wd/hub"
        )

        # Waits for the driver to be setup.
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
