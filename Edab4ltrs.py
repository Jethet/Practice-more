# Create a function that takes a list of strings.
# Return all words in the list that are exactly four letters.

def isFourLetters(lst):
    my_list = []
    for x in lst:
        if len(x) == 4:
            my_list.append(x)
    return my_list


print(isFourLetters(["Ryan", "Kieran", "Jason", "Matt" ])) # ["Ryan", "Matt"]

print(isFourLetters(["Tomato", "Potato", "Pair"]))      # ["Pair"]

print(isFourLetters(["Kangaroo", "Bear", "Fox"]))       # ["Bear"]
