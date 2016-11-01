# CodingBat / Python / String-1 / "combo_string"
# URL -- http://codingbat.com/prob/p194053

"""
Given 2 strings, a and b, return a string in the form of 'short+long+short',
with the shorter string on the outside and the longer string on the inside.
The strings will not be the same length, but they may be empty (length 0).
combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'
"""

# My original solution
def combo_string(a, b):
    if len(a) > len(b):
        long = a[:]
        short = b[:]
    else:
        long = b[:]
        short = a[:]
    return short + long + short


# Alternative solution, later
def combo_string(a, b):
    if len(a) < len(b):
        return a+b+a
    else:
        return b+a+b