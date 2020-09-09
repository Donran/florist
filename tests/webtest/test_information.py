import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class InformationTest(WebTestBase.BaseTest):

    # Tests if website contains address information
    def test_address_found(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        address = """Fjällgatan 32H
981 39 KIRUNA"""

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

        if(len(opening_hours_elems) > 0):
            for index in range(len(opening_hours_elems)):
                open_hour_text = opening_hours_elems[index].get_attribute("innerHTML")
                if(index >= len(open_hours)):
                    index = index - len(open_hours)
                    self.assertEqual(open_hour_text, open_hours[index])
                else:
                    self.assertEqual(open_hour_text, open_hours[index])
        else:
            self.fail("No opening hours found")

    # Tests if website contains email and phonenumber
    def test_email_and_phonenumber_found(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        email = "info@DOMÄN"
        phonenumber = "0630-555-555"


        try:
            driver.find_element(By.PARTIAL_LINK_TEXT, email)
        except NoSuchElementException:
            self.fail("No email found")


        try:
            driver.find_element(By.PARTIAL_LINK_TEXT, phonenumber)
        except NoSuchElementException:
            self.fail("No phonenumber found")

    # Test som kollar om hemsidan innehåller en
    # <h1 class="title"> med texten "Välkommen till Floristgården!"
    def test_text_exist(self):
        validText = "Välkommen till Floristgården!"
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        elem = driver.find_element(By.CLASS_NAME, "display-4")
        self.assertEqual(validText, elem.text)


    # Test som kollar om hemsidans title innehåller "Floristgården"
    def test_title_exist(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        validTitle = "Floristgården"
        self.assertIn(validTitle, driver.title)
