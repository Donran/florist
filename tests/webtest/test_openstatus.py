import WebTestBase
import requests, datetime, time, yaml
from os import path
from selenium.webdriver.common.by import By
class OpenStatusTest(WebTestBase.BaseTest):
    def test_openStatusText(self):
        yaml_file = open("../../site/_data/open_days.yml")
        parsed_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)
        yaml_file.close()

        driver = self.driver
        driver.get(self.WEBSITE_URL)
        test_dates = [
            datetime.date(2020, 9, 14), # Monday
            datetime.date(2021, 4, 13), #Tuesday
            datetime.date(2020, 12, 24), #Thursday
            datetime.date(2020, 12, 26), #Saturday
            datetime.date(2020, 12, 27) #Sunday
        ]
        for date in test_dates:
            date_string = f"{date.year}, {date.month - 1}, {date.day}"
            injected_javascript = (
                f'openBanner(new Date({date_string}))'
            )
            # Injects script that simulates the date we want.
            driver.execute_script(injected_javascript)
            driver.implicitly_wait(3)

            day_index = 0 if date.weekday() < 5 else date.weekday() - 4

            status = driver.find_element(By.ID, "open-banner")
            if parsed_yaml[day_index]['time'].lower() not in status.text:
                self.fail(f"Wrong hours are showing ({parsed_yaml[day_index]['time']}, {status.text})")





