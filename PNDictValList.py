# Given a dictionary get all values from the dictionary and add these to a list
# but don’t add duplicates

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53,
      'July':54, 'Aug':44, 'Sept':54}

val_list = []
for value in speed.values():
    if value not in val_list:
        val_list.append(value)
print(val_list)


# Expected Outcome: [47, 52, 44, 53, 54]
