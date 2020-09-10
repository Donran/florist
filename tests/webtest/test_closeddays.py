import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
class ClosedDaysTest(WebTestBase.BaseTest):

    def test_closeddays(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"hitta_hit.html")
        driver.implicitly_wait(5)
        closeddays_dates = [
            "nyårsdagen: 1 januari",
            "trettondedag jul: 6 januari",
            "första maj: 1 maj",
            "sveriges nationaldag: 6 juni",
            "julafton: 24 december",
            "juldagen: 25 december",
            "annandag jul: 26 december",
            "nyårsafton: 31 december"
        ]
        driver.implicitly_wait(3)
        closeddays = driver.find_elements(By.CLASS_NAME, "closed-day")

        self.assertEqual(len(closeddays), len(closeddays_dates))

        for day in closeddays:
            day_on_site = day.text.lower()
            if day_on_site not in closeddays_dates:
                self.fail("Could not find employee in list: " + day_on_site)
