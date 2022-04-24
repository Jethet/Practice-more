import datetime

# Define methods to calculate the number of dates until a specified date

def header():
  print("-------------------------------------")
  print("Calculate the date difference in days")
  print("-------------------------------------")

def get_birthday():
  print("Let's fill in when were you born")
  year = int(input("What year were you born?: "))
  month = int(input("What month were you born?: "))
  day = int(input("What day were you born?: "))

  birthdate = datetime.date(year, month, day)
  return birthdate
  
def compare_dates(original_date, target_date):
  current = datetime.date(original_date.year, original_date.month, original_date.day)
  dt = current - target_date
  return dt.days

def printdays(days):
  if days < 0:
    print("You had your birthday {} days ago".format(-days))
  elif days > 0:
    print("Your birthday is in {} days".format(days))
  else:
    print("CONGRATULATIONS!")

# Define main method
def main():
  header()
  existing_date = get_birthday()
  print(str(existing_date))
  today = datetime.date.today()
  print(str(today))
  numofdays = compare_dates(existing_date, today)
  print(str(numofdays))
  printdays(numofdays)

main()