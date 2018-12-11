#given an int n, return True if it is within 10 of 100 or 200. ( abs(n) )

def near100(n):
    return (abs(n) >= 90 and abs(n) <= 110 or abs(n) >= 190 and abs(n) <= 210)

print(near100(89))
