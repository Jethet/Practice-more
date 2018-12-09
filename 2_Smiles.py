#Two monkeys a and b plus parameters a_smile and b_smile to indicate
#  if they are smiling. If both are smiling or none of them: True
#  otherwise: False

def smiles(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False
