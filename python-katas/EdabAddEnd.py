# Create a function that adds a string ending to each member in a list.

def add_ending(lst, ending):
    result = [x + ending for x in lst]
    return result


print(add_ending(["clever", "meek", "hurried", "nice"], "ly"))
#➞ ["cleverly", "meekly", "hurriedly", "nicely"]
print(add_ending(["new", "pander", "scoop"], "er"))
#➞ ["newer", "panderer", "scooper"]
print(add_ending(["bend", "sharpen", "mean"], "ing"))
#➞ ["bending", "sharpening", "meaning"]
