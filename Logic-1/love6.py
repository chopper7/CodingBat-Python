# Coding Bat / Python / Logic-1 / "love6"
# URL -- http://codingbat.com/prob/p100958

"""
The number 6 is a truly great number. Given two int values, a and b, return
True if either one is 6. Or if their sum or difference is 6.
love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
"""

def love6(a, b):
    sum_nums = a+b
    diff_nums = abs(a-b)
    return 6 in (a, b, sum_nums, diff_nums)

