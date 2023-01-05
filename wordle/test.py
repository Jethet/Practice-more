# word = "metal"
# guess = "dream"
green = '\033[92m'

# indexWord = [i for i, c in enumerate(word)]
# indexGuess = [i for i, b in enumerate(guess)]

# for x in guess:
#     if x in word:
#         indexX = [i for i, d in enumerate(word) if d == x]
#         for y in indexX:
#             if y in indexX:
#                 print(f'{green}', y)

word = "toast"
guess = "guest"
for x in word:
    if x in guess:
        indexGuessChar = [i for i, b in enumerate(guess) if b == x]
        indexWordChar = [i for i, a in enumerate(word) if a == x]
        for b in indexGuessChar:
            for a in indexWordChar:
                if b == a:        
                    print(f'{green}', x)
                else:
                    print("wrong")
    

        