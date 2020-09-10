import datetime
import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import tracemalloc

tracemalloc.start()

def get_day_difference(day):
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

	current_date = datetime.date.today()

	day_arr = day.split(" ")
	month = MONTHS_TO_NUM[day_arr.pop()]
	date_num = int(day_arr.pop())
	year = int(current_date.year)

	if(month < current_date.month):
		year+=1

	day_date = datetime.date(year, month, date_num)

	delta = day_date - current_date

	return [delta.days, day]

def get_sorted_closed_days(closed_days):
	closed_days_dates = list(map(get_day_difference, closed_days))

	temp_sorted = sorted(closed_days_dates,key=lambda x: x[0])
	return list(map(lambda d: d[1], temp_sorted)) # Removes the day difference from list

class ClosedDaysTest(WebTestBase.BaseTest):

    def test_closeddays(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"hitta_hit.html")

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
            td_elems = day.find_elements(By.TAG_NAME, "td")
            day_on_site = f"{td_elems[0].text}: {td_elems[1].text}".lower()
            if day_on_site not in closeddays_dates:
                self.fail("Could not find day in list: " + day_on_site)

    def test_closedays_ordered(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"hitta_hit.html")

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
        sorted_days = get_sorted_closed_days(closeddays_dates)

        driver.implicitly_wait(3)
        closeddays = driver.find_elements(By.CLASS_NAME, "closed-day")

        for i in range(len(closeddays)):
            td_elems = closeddays[i].find_elements(By.TAG_NAME, "td")
            day_on_site = f"{td_elems[0].text}: {td_elems[1].text}".lower()
            
            if day_on_site != sorted_days[i]:
                self.fail("Wrong order in list.")
