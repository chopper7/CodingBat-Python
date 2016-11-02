# CodingBat / Python / Logic-2 / "make_bricks"
# URL -- http://codingbat.com/prob/p118406

"""
We want to make a row of bricks that is goal inches long. We have a number of
small bricks (1 inch each) and big bricks (5 inches each). Return True if it is
possible to make the goal by choosing from the given bricks. This is a little
harder than it looks and can be done without any loops.
make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
make_bricks(7, 1, 11) → True
make_bricks(22, 2, 33) → False

See:  http://codingbat.com/doc/practice/makebricks-introduction.html
"""

def make_bricks(small, big, goal):
    # If too few big bricks to reach goal...
    if big*5 < goal:
        # Can you add enough small bricks to the bigs to reach goal?
        return big*5 + small >= goal
    # Otherwise you have enough big bricks, so use just enough to get within
    # 5 bricks of goal without exceeding it, then try adding small bricks
    else:
        # How many big bricks can be used without exceeding goal?
        bigs_used = goal/5
        # Add smalls to bigs to see if there's enough of both to reach the goal
        return bigs_used*5 + small >= goal
