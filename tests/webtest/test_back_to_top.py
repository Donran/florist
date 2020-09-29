import WebTestBase
from selenium.webdriver.common.by import By

class BackToTopTest(WebTestBase.BaseTest):    
    def test_back_to_top_text(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        validInfo = "Tillbaka till toppen"
        elem = driver.find_element(By.CLASS_NAME, "back-to-top")
        self.assertIn(validInfo, elem.text)



    def test_back_to_top_works(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        back_to_top = driver.find_element(By.CLASS_NAME, "back-to-top")
        at_top = driver.execute_script("""
                    arguments[0].scrollIntoView(true);
                    arguments[0].click();
                    return window.scrollY == 0;""", back_to_top
                )

        self.assertTrue(at_top)

