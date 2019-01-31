# Create a function that takes a number as an argument and returns a string
# formatted to separate thousands.

def format_num(n):
    n = str(n)
    if len(n) >= 7:
        return n[0:-6] +  ',' + n[-6:-3] + ',' + n[-3::]
    if len(n) >= 4:
        return n[0:-3] + ',' + n[-3::]
    else:
        return n



print(format_num(1000)) # "1,000"

print(format_num(100000)) # "100,000"

print(format_num(20)) # "20"
