x = int(input("Please enter your first number: "))
y = int(input("Please enter your second number: "))
method = input("Please choose your caculator method: add/substract/divide/multiply: ")

match method:
  case "add":
    print("The result of the addition is:", x + y)
  case "substract":
    print("The result of the substraction is:", x - y)
  case "divide":
    print("The result of the division is:", x / y)
  case "multiply":
    print("The result of the multiplication is:", x * y)
  case _:
    print("Invalid operation")
