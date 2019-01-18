# Create a function that accepts a Date object and returns True if
# it's Christmas Eve (December 24th) and False otherwise.

# WHAT IS A DATE OBJECT? WHY IS THE FORMATTING IN THE EXAMPLES STRANGE (SPACES)?

def datetime(date):
    if '12' and '24' in date:
        return True
    else:
        return False


print(datetime.date( 2013, 12, 24 )) # True

print(datetime.date( 2013, 1, 23 ))  # False

print(datetime.date( 3000, 12, 24 )) # True
