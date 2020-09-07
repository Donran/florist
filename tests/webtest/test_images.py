import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class ImagesTest(WebTestBase.BaseTest):
    # Test to make sure all links are present
    def test_images(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        images = None
        try:
            images = driver.find_element(By.CLASS_NAME, "product-images")
            children = images.find_elements(By.XPATH, "//img")
        except NoSuchElementException:
            self.fail("No images found.")
        self.assertGreaterEqual(len(children), 3)

