word = "metal"
guess = "dream"
green = '\033[92m'

indexWord = [i for i, c in enumerate(word)]
indexGuess = [i for i, b in enumerate(guess)]

for x in guess:
    if x in word:
        indexX = [i for i, d in enumerate(word) if d == x]
        for y in indexX:
            if y in indexX:
                print(f'{green}', y)
