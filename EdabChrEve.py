# Create a function that accepts a Date object and returns True if
# it's Christmas Eve (December 24th) and False otherwise.

from datetime import date

def time_for_milk_and_cookies(date):
    return datetime.date(2019, 12, 24)



print(time_for_milk_and_cookies( 2013, 12, 24 )) # True
print(time_for_milk_and_cookies( 2013, 1, 23 ))  # False
print(time_for_milk_and_cookies( 3000, 12, 24 )) # True
