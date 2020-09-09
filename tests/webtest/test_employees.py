import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class EmployeeTest(WebTestBase.BaseTest):
    def test_names_and_roles(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"/personal.html")

        employees = driver.find_elements(By.CLASS_NAME, "employee")
        self.assertEqual(len(employees), 3)

        emloyee_names = [
            "Anna Pettersson",
            "Fredrik Ortqvist",
            "Örjan Johansson"
        ]

        employee_roles = [
            "Horticulturist",
            "Owner",
            "Florist"
        ]

        for employee in employees:
            name_on_site = employee.find_element(By.CLASS_NAME, "employee-name").text
            role_on_site = employee.find_element(By.CLASS_NAME, "employee-role").text

            if name_on_site not in emloyee_names:
                self.fail("Could not find employee in list: " + name_on_site)

            if role_on_site not in employee_roles:
                self.fail("Could not find role in list: " + role_on_site)
