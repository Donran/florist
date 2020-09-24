import WebTestBase
from selenium.webdriver.common.by import By

class EmployeeWelcomeTest(WebTestBase.BaseTest):    
    def test_welcome(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"/personal.html")
        welcometxt = driver.find_element(By.CLASS_NAME, "employee_welcome").text
        txt_in_class = ("Välkommen till oss på Floristgården! Vi är ett sammansvetsat gäng med olika expertkompetenser som därmed kan hjälpa dig på bästa sätt utifrån dina behov.")

        if welcometxt == txt_in_class:
            True
        else:
            self.fail("Could not find Welcome text")