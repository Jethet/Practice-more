#Given a string, return new string with first and last chars exchanged

def front_back(str):
    str = str[-1] + str[1:-1] + str[0]
    return str

print(front_back('2'))
