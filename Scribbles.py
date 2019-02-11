
def get_middle_char(str):
    length = len(str)
    return str[(length / 2) + (length % 2) - 1]

print(get_middle_char('whatevery'))

#('123', '4', '567')
