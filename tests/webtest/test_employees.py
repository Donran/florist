import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class EmployeeTest(WebTestBase.BaseTest):
    def test_names(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"/personal.html")

        employees = driver.find_elements(By.CLASS_NAME, "employee")
        self.assertEqual(len(employees), 3)

        names = [
            "Anna Pettersson",
            "Fredrik Ortqvist",
            "Örjan Johansson"
        ]
        for employee in employees:
            name_on_site = employee.find_element(By.CLASS_NAME, "employee-name").text
            if name_on_site not in names:
                self.fail("Could not find employee in list: " + name_on_site)

