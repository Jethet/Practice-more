# Given a non-empty string like "Code" return a string like "CCoCodCode".

def str_plosion(str):
    result = ""
  # On each iteration, add the substring of the chars 0..i
    for i in range(len(str)):
        result = result + str[:i+1]
    return result

print(str_plosion('code'))
print(str_plosion('abc'))
print(str_plosion('ab'))
