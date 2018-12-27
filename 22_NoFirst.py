# Given 2 strings, return their concatenation without first char of each.

def non_start(a, b):
    return a[1:] + b[1:]



print(non_start('Hello', 'there'))
