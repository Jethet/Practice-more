# Write a function that takes four string arguments. You will be comparing the
# first string to the three next strings. Verify if the first string starts
# with the second string, includes the third string, and ends with the fourth
# string. If the first string passes all checks, return the string "My head,
# body, and tail.", otherwise, return "Incomplete.".

def verify_substrs(main_txt, head, body, tail):
    if main_txt.startswith(head) and main_txt.endswith(tail) and body in main_txt:
        return "My head, body, and tail."
    else:
        return "Incomplete."



print(verify_substrs("Onomatopeia", "on", "mato", "ia")) # "Incomplete."

print(verify_substrs("Centipede", "Cent", "tip", "pede")) # "My head, body, and tail."

print(verify_substrs("apple", "AP", "PPL", "LE")) # "Incomplete."
