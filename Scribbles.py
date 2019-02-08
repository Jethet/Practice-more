def change(txt):
    if 'a' in txt:
        txt.replace('a', '4')
    return txt

str = 'acht'
str.replace('a', '4')
print(str)
