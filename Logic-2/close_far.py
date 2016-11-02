# CodingBat / Python / Logic-2 / "close_far"
# URL -- http://codingbat.com/prob/p160533

"""
Given three ints, a b c, return True if one of b or c is "close" (differing
from a by at most 1), while the other is "far", differing from both other
values by 2 or more. Note: abs(num) computes the absolute value of a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
close_far(-1, 10, 0) → True
"""

def close_far(a, b, c):
    # Condition 1: the "close" tests
    btest = abs(a-b) <= 1
    ctest = abs(a-c) <= 1
    # they can't both be within 1 of value a
    cond1 = btest != ctest
    
    # Condition 2: the "far" tests
    if btest == False:
        # test b for farness
        cond2 = abs(a-b) >= 2 and abs(c-b) >= 2
    if ctest == False:
        # test c for farness
        cond2 = abs(a-c) >= 2 and abs(b-c) >= 2
  
    # Are both conditions met?
    return cond1 and cond2