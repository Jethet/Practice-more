# Create a function that takes in three arguments (prob, prize, pay) and returns
# True if prob * prize > pay; otherwise return False.
#A profitable gamble is a game that yields a positive net profit, where net profit
# is calculated in the following manner:
#    net_outcome = probability_of_winning * prize - cost_of_playing.
# To illustrate, profitable_gamble(0.2, 50, 9) should yield true, since the net
# profit is 1 (0.2 * 50 - 9), and 1 > 0.

def profitable_gamble(prob, prize, pay):
    if prob * prize > pay:
        return True
    else:
        return False

print(profitable_gamble(0.2, 50, 9)) #➞ True
print(profitable_gamble(0.9, 1, 2)) #➞ False
print(profitable_gamble(0.9, 3, 2)) #➞ True
