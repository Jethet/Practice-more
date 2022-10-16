# Return number of times 'code' appears in given string but 'd' can be
# replaced by any letter.

def count_code(str):
    count = 0
    for i in range(len(str)-3):      # i is third position (of 'code')
        if str[i:i+2] == 'co' and str[i+3] == 'e':  # i+2 can be 'co'
            count += 1                             # while i+3 can be 'e'
    return count



print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))
