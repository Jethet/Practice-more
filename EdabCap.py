# Create a function that takes a list of names and returns a list with the
# first letter capitalized. Order of the original list cannot be changed.
# Note: MABELLE is returned Mabelle


def cap_me(lst):
    new_lst = [x.lower() for x in lst]
    return [x.capitalize() for x in new_lst]


print(cap_me(["mavis", "senaida", "letty"])) # ["Mavis", "Senaida", "Letty"]
print(cap_me(["samuel", "MABELLE", "letitia", "meridith"])) # ["Samuel", "Mabelle", "Letitia", "Meridith"]
print(cap_me(["Slyvia", "Kristal", "Sharilyn", "Calista"])) # ["Slyvia", "Kristal", "Sharilyn", "Calista"]
