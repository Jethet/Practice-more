# Commonly used classes in the datetime module are:
#  date Class
#  time Class
#  datetime Class
#  timedelta Class

import datetime

# One of the classes defined in the datetime module is the datetime class.
# By using the now() method you create a datetime object with current
# local date and time.
datetime_object = datetime.datetime.now()
print(datetime_object)

# By using the today() method, defined in the date class, you get a date
# object with the current local date.
date_object = datetime.date.today()
print(date_object)

# You can instantiate date objects from the date class. A date object
# represents a date (year, month, day). date() is a constructor and
# takes 3 arguments: year, month and day.
d = datetime.date(2019, 4, 13)
print(d)

# To import date class, use the datetime module:
from datetime import date
a = date(2019, 1, 1)
print(a)

# To get the current date, use today() :
from datetime import date
today = date.today()
print("The current day is", today)

# Same goes for today.year and today.day:
print(today.year)
print(today.month)

"""
mydate = datetime.date(1943,3, 13) #year, month, day
print(mydate.strftime("%A"))
"""
