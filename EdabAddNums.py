# Create a function that takes a number as an argument. Add up all the numbers
# from 1 to the number you passed to the function. For example, if the input
# is 4 then your function should return 10 because 1 + 2 + 3 + 4 = 10.


def add_up(num):
    return sum(range(num+1))    # num+1 because otherwise the count stops
                                # before num: now the count stops before +1




print(add_up(4))   # 10

print(add_up(13))  # 91

print(add_up(600)) # 180300
