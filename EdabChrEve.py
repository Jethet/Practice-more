# Create a function that accepts a Date object and returns True if
# it's Christmas Eve (December 24th) and False otherwise.

import datetime

def time_for_milk_and_cookies(date):
    if date.month == 12 and date.day == 24:
        return True
    else:
        return False



print(time_for_milk_and_cookies( 2013, 12, 24 )) # True
print(time_for_milk_and_cookies( 2013, 1, 23 ))  # False
print(time_for_milk_and_cookies( 3000, 12, 24 )) # True
