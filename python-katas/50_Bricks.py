# We want to make a row of bricks that is 'goal' inches long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make goal by choosing from the given bricks.
# This is a little harder than it looks and can be done without any loops.

def make_bricks(small, big, goal):
    if goal > small + big * 5:
        return False
    else:
        return goal % 5 <= small

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))
