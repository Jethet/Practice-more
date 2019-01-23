# Create a function that takes a string and returns a new string with all vowels
# removed. "y" is not considered a vowel.

def silence_Trump(txt):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_txt = []
    for x in txt:
        if x.lower() not in vowels:
            new_txt.append(x)
    return ''.join(new_txt)




print(silence_Trump("I have never seen a thin person drinking Diet Coke.")) # " hv nvr sn  thn prsn drnkng Dt Ck."

print(silence_Trump("We're gonna build a wall!")) # "W'r gnn bld  wll!"

print(silence_Trump("Happy Thanksgiving to all--even the haters and losers!")) # "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"
