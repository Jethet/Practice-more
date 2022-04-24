from secrets import choice


print("Welcome to Basic Calc")


# # first number
# x = int(input("Please enter your first number: "))

# # second number
# y = int(input("Please enter your second number: "))

# # add numbers
# result = x + y

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

# output numbers
# print("This is the result:", add(2, 4))

# Create menu to select:
print("Choose what you want to do:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
  choice = input("Enter input number 1/2/3/4: ")
  if choice in ("1", "2", "3", "4"):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == "1":
      print(add(num1, num2))
    elif choice == "2":
      print(subtract(num1, num2))
    elif choice == "3":
      print(multiply(num1, num2))
    elif choice == "4":
      print(divide(num1, num2))
    break
  else:
    print("You did not enter valid input, try again.")