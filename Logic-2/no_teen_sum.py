# CodingBat / Python / Logic-2 / "no_teen_sum"
# URL -- http://codingbat.com/prob/p100347

"""
Given 3 int values, return their sum. However, if any of the values is a teen
-- in the range 13..19 inclusive -- then that value counts as 0, EXCEPT 15 and
16 do not count as a teens.
Write a separate helper 'def fix_teen(n)' that takes in an int value and 
returns that value fixed for the teen rule. In this way, you avoid repeating 
the teen code 3 times (i.e. 'decomposition'). Define the helper below and at
the same indent level as the main 'no_teen_sum()' function.
no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
"""
# my note: this problem would make more sense if the ints were in a list

def fix_teen(n):
    '''Takes an int value and returns it fixed for the 15&16 teen rule'''
    if n in (13, 14, 17, 18, 19):
        return 0
    else:
        return n

def no_teen_sum(a, b, c):
    '''
    Given three ints, a b c, return their sum. 
    If any of the values is a teen -- in the range 13..19 inclusive -- 
    then that value counts as 0, except 15 and 16.
    '''
    # Check each int to see if it should be set to 0. Then sum all the ints.
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
