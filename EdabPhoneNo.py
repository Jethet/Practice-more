# Create a function that takes a list of 10 numbers (between 0 and 9) and
# returns a string of numbers formatted as a phone number e.g. (555) 555-5555.

def format_phone_number(lst):
    x = str("".join(str(lst[0:3])))
    y = str("".join(str(lst[3:6])))
    z = str(''.join(str(lst[6::])))
    return str('(' + x.lstrip('[').rstrip(']').replace(', ','') + ')' + ' ' + \
            y.lstrip('[').rstrip(']').replace(', ','') + '-' + \
            z.lstrip('[').rstrip(']').replace(', ',''))

# From Edabit:
def format_phone_number(lst):
  return '({}{}{}) {}{}{}-{}{}{}{}'.format(*lst)

print(format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # "(123) 456-7890"
print(format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8])) # "(519) 555-4468"
print(format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7])) # "(345) 501-2527"
