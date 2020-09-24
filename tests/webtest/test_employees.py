import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class EmployeeTest(WebTestBase.BaseTest):
    def test_names_and_roles(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"/personal.html")

        employees = driver.find_elements(By.CLASS_NAME, "employee")
        self.assertEqual(len(employees), 3)

        employee_names = [
            "Anna Pettersson",
            "Fredrik Ortqvist",
            "Örjan Johansson"
        ]

        employee_roles = [
            "Hortonom",
            "Ägare",
            "Florist"
        ]

        emloyee_msg = [
            "Jag är utbildad hortonom och kan hjälpa dig eller ditt företag att göra det bästa valet utifrån dina behov och förutsättningar vad det gäller fruktträd, grönsaksodling och prydnadsväxter.",
            "Min kärlek till blommor lade grunden till att Floristgården finns idag och jag hoppas att du som kund kan inspireras i vår butik.",
            "Om du behöver en bukett, oavsett om det är till bröllop, födelsedagsfirande eller något helt annat kan jag hjälpa dig att komponera buketten utifrån dina önskemål."
        ]
        

        for employee in employees:
            name_on_site = employee.find_element(By.CLASS_NAME, "employee-name").text
            role_on_site = employee.find_element(By.CLASS_NAME, "employee-role").text
            msg_on_site = employee.find_element(By.CLASS_NAME, "employee-msg").text

            if name_on_site not in employee_names:
                self.fail("Could not find employee in list: " + name_on_site)

            if role_on_site not in employee_roles:
                self.fail("Could not find role in list: " + role_on_site)
            
            if msg_on_site not in emloyee_msg:
                self.fail("Could not find employees message in list: " + msg_on_site)
