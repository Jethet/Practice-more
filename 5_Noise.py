#Parrot noise: before 7 or after 20 return True. Parameters: hour and noise

def parrot(noise, hour):
    if noise is True:
        if hour < 7 or hour > 20:
            return True
    if noise is False:
        return False
    else:
        return False


print(parrot(True, 7))
print(parrot(True, 20))
