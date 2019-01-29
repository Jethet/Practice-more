# Create a function that takes a list of numbers and returns its median.
# Input can be any negative or positive number. List being passed will contain
# at least four numbers.
import statistics

def median(lst):
    return statistics.median(lst)



print(median([2, 5, 6, 2, 6, 3, 4])) # 4

print(median([21.4323, 432.54, 432.3, 542.4567])) # 432.4

print(median([-23, -43, -29, -53, -67])) # -43
