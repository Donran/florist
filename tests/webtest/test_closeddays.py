#import WebTestBase
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
from datetime import date
import datetime


date1 = date(2020,1,1)
date2 = date(2020,1,6)
date3 = date(2020,5,1)
date4 = date(2020,6,6)
date5 = date(2020,12,24)
date6 = date(2020,12,25)
date7 = date(2020,12,26)
date8 = date(2020,12,31)

Today = datetime.date.today()

days = [date1, date2, date3, date4, date5, date6, date7, date8]

def countdays():
    for date in days:
        delta = date - Today
        print("Day diff: {}".format(delta))


countdays()


#1 januari
#6 januari
#1 maj
#6 juni
#24 december
#25 december
#26 december
#31 december
