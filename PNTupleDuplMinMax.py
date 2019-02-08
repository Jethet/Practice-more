# Remove duplicate from a list and create a tuple and find the minimum and
# maximum number

sampleList = [87, 45, 41, 65, 94, 41, 99, 94]

single_tup = []
for value in sampleList:
    if value not in single_tup:
        single_tup.append(value)
final_tup = tuple(single_tup)
print(single_tup)
print(final_tup)
print(min(final_tup))
print(max(final_tup))

# Expected Outcome:
# unique items [87, 45, 41, 65, 94, 99]
# tuple (87, 45, 41, 65, 94, 99)
# min: 41
# max: 99
