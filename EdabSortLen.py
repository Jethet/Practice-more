# Create a function that takes a list of strings and return a list, sorted
# from shortest to longest.
# Both list.sort() and sorted() have a key parameter to specify a function
# to be called on each list element prior to making comparisons.

def sort_by_length(lst):
    return sorted(lst, key = len)


print(sort_by_length(["Google", "Apple", "Microsoft"])) # ["Apple", "Google", "Microsoft"]
print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"])) # ["Raphael", "Leonardo", "Donatello", "Michelangelo"]
print(sort_by_length(["Turing", "Einstein", "Jung"])) # ["Jung", "Turing", "Einstein"]
