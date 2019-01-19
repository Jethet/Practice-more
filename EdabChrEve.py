# Create a function that accepts a Date object and returns True if
# it's Christmas Eve (December 24th) and False otherwise.

def datetime(date):
    return datetime.date(2019, 12, 24)



print(datetime.date( 2013, 12, 24 )) # True

print(datetime.date( 2013, 1, 23 ))  # False

print(datetime.date( 3000, 12, 24 )) # True
