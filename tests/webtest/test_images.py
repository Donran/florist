import WebTestBase
from selenium.webdriver.common.by import By
class ImagesTest(WebTestBase.BaseTest):
    # Test to make sure all links are present
    def test_images(self):
        driver = self.driver
        driver.get(SELF.WEBSITE_URL)
        images = None
        try:
            images = driver.find_element(By.CLASS_NAME, "image")
        except NoSuchElementException:
            self.fail("No images found.")
        self.assertGreaterEqual(len(iamges), 3)

