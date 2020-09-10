import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class ClosedDaysTest(WebTestBase.BaseTest):

    def test_closeddays():
        driver = self.driver
        driver.get(self.WEBSITE_URL+"/hittahit.html")
        closeddays_dates = [
            "Nyårsdagen: 1 Januari",
            "Trettondedagen: 6 Januari",
            "Första Maj: 1 Maj",
            "Sveriges Nationaldag, 6 Juni",
            "Julafton: 24 December",
            "Juldagen: 25 December",
            "Annandag Jul: 26 December",
            "Nyårsafton: 31 December"
        ]
        closeddays = driver.find_elements(By.CLASS_NAME, "closed-day")
        self.assertEqual(len(closeddays), len(closeddays_dates))

        for day in closeddays:
            day_on_site = day.text

            if day_on_site not in closeddays_dates:
                self.fail("Could not find employee in list: " + day_on_site)

           

        
        
        
    