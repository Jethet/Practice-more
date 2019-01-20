# Create a function that takes a list of unsorted numbers between 1 and 10
# (excluding one number) and returns the missing number.

def missing_nums(lst):
    total_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in total_lst:
        if x not in lst:
            return x

# Edabit:
def missing_nums(lst):
  for n in range(1,11):
    if n not in lst:
      return(n)

print(missing_nums([1, 2, 3, 4, 6, 7, 8, 9, 10])) # 5
print(missing_nums([7, 2, 3, 6, 5, 9, 1, 4, 8])) # 10
print(missing_nums([10, 5, 1, 2, 4, 6, 8, 3, 9])) # 7
