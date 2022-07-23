from pprint import pprint

x = int(input("Please enter your first number: "))
y = int(input("Please enter your second number: "))
method = input("Please choose your caculator method: add/substract/divide/multiply: ")

def calculate(x, y):
  if method == "add":
    print("The result of the addition is:", x + y)
  elif method == "substract":
    print("The result of the substraction is:", x - y)
  elif method == "divide":
    print("The result of the division is:", x / y)
  elif method == "multiply":
    print("The result of the multiplication is:", x * y)
  else:
    print("Invalid operation")

calculate(x, y)