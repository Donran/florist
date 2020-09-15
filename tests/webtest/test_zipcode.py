import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class ZipCodeTest(WebTestBase.BaseTest):

    # Test to make sure zipcode theme exists
    def test_zipcode_field_exists(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        try:
            zipcode_input = driver.find_element(By.ID, "zipcode")
        except NoSuchElementException:
            self.fail("No zipcode found.")

    # Test to make sure it returns success message on valid zipcode
    def test_zipcode_valid_input(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        valid_inputs = ["981 39", "981 40", "981 42", "981 38"]

        zipcode_input = driver.find_element(By.ID, "zipcode")
        zipcode_btn = driver.find_element(By.ID, "zipcode-btn")

        for valid_input in valid_inputs:
            zipcode_input.clear()
            zipcode_input.send_keys(valid_input)
            zipcode_btn.click()
            assert "Vi skickar blommor inom detta postnummer." in driver.page_source


    # Test to make sure it returns error message on invalid zipcode
    def test_zipcode_invalid_input(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        zipcode_input = driver.find_element(By.ID, "zipcode")
        zipcode_input.clear()
        zipcode_input.send_keys("blah blah")

        zipcode_btn = driver.find_element(By.ID, "zipcode-btn")
        zipcode_btn.click()

        assert "Vi skickar inte blommor inom detta postnummer." in driver.page_source

    def test_zipcode_enter_is_pressed(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        zipcode_input = driver.find_element(By.ID, "zipcode")
        zipcode_input.clear()

        zipcode_input.send_keys("98139")
        zipcode_input.send_keys(Keys.ENTER)
        assert "Vi skickar blommor inom detta postnummer." in driver.page_source