# Given 3 int values, a b c, return their sum. If one of the values is the same
# as another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
    if a == b and a == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c


# CodingBat:

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a # This is shorthand for: sum = sum + a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c

  return sum

print(lone_sum(1, 2, 3)) # 6
print(lone_sum(3, 2, 3)) # 2
print(lone_sum(3, 3, 3)) # 0
