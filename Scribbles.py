# Find out about this code:

def format_phone_number(lst):
  return '({}{}{}) {}{}{}-{}{}{}{}'.format(*lst)


txt = 'Not a palindrome'
txt2 = txt[::-1]
print(txt, txt2)
print(txt.islower() == txt2.islower())
