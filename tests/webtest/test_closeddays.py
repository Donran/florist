import yaml
import datetime, time
import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def get_day_difference(day, test_date):
    MONTHS_TO_NUM = {
        "januari": 1,
        "februari": 2,
        "mars": 3,
        "april": 4,
        "maj": 5,
        "juni": 6,
        "juli": 7,
        "augusti": 8,
        "september": 9,
        "oktober": 10,
        "november": 11,
        "december": 12
    }


    day_arr = day.split(" ")
    month = MONTHS_TO_NUM[day_arr.pop()]
    date_num = int(day_arr.pop())
    year = int(test_date.year)

    if month == test_date.month:
        if date_num < test_date.day:
            year+=1
    elif month < test_date.month:
	    year+=1

    day_date = datetime.date(year, month, date_num)

    delta = day_date - test_date

    return [delta.days, day]

def get_sorted_closed_days(closed_days, test_date):
	closed_days_dates = list(map(lambda day: get_day_difference(day, test_date), closed_days))

	temp_sorted = sorted(closed_days_dates,key=lambda x: x[0]) # Returns closed_days sorted with a day_diff.
	return list(map(lambda d: d[1], temp_sorted)) # Removes the day difference from list

def get_closed_days():
    yaml_file = open("../../site/_data/closed_days.yml")
    parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
    yaml_file.close()
    return list(map(lambda closedday: closedday.get("name") + ": " + closedday.get("day"), parsed_yaml_file))

class ClosedDaysTest(WebTestBase.BaseTest):

    def test_closeddays(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"hitta_hit.html")

        closeddays_dates = get_closed_days()

        driver.implicitly_wait(3)
        closeddays = driver.find_elements(By.CLASS_NAME, "closed-day")

        self.assertEqual(len(closeddays), len(closeddays_dates))

        for day in closeddays:
            td_elems = day.find_elements(By.TAG_NAME, "td")
            day_on_site = f"{td_elems[0].text}: {td_elems[1].text}"
            if day_on_site not in closeddays_dates:
                self.fail("Could not find day in list: " + day_on_site)

    def test_closeddays_ordered(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"hitta_hit.html")

        closeddays_dates = get_closed_days()

        # List with different dates to simulate
        test_dates = [
            datetime.date(2020, 9, 14),
            datetime.date(2021, 4, 13),
            datetime.date(2020, 12, 24),
            datetime.date(2020, 12, 26)
        ]

        # Tests with different simulated dates
        for test_date in test_dates:
            sorted_days = get_sorted_closed_days(closeddays_dates, test_date)

            # The JavaScript that we want to inject.
            # We simulate the time with a library called sinonJs that gets imported in our
            # hitta_hit.html
            date_string = f"{test_date.year}, {test_date.month - 1}, {test_date.day}"
            injected_javascript = (
                f'updateClosedDays(new Date({date_string}))'
            )
            # Injects script that simulates the date we want.
            driver.execute_script(injected_javascript)

            driver.implicitly_wait(3)
            closeddays = driver.find_elements(By.CLASS_NAME, "closed-day")

            for i in range(len(closeddays)):
                td_elems = closeddays[i].find_elements(By.TAG_NAME, "td")
                day_on_site = f"{td_elems[0].text}: {td_elems[1].text}"

                if day_on_site != sorted_days[i]:
                    self.fail(f"Wrong order in list. Date: {test_date}")
