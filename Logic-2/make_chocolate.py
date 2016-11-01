# CodingBat / Python / Logic-2 / "make_chocolate"
# URL -- http://codingbat.com/prob/p190859

"""
We want make a package weighing `goal` kilos of chocolate. We have small bars
(1 kilo each) and big bars (5 kilos each). Return the number of small bars to
use, assuming we always use big bars before small bars. Return -1 if it can't
be done.
make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
make_chocolate(60, 100, 550) → 50
"""

def make_chocolate(small, big, goal):
    # How much is weight shy of goal after using big bars?
    wt_remaining = goal % 5
    # Combined weight of big bars
    wt_bigs = big * 5
    
    # How many small bars shall we use?
    if small >= wt_remaining and wt_bigs >= goal:
        return wt_remaining
    elif wt_bigs < goal and small >= goal - wt_bigs:
        return goal - wt_bigs
    else:
        return -1
