# Coding Bat / Python / Warmup-2
# All problems from this section are included in this script.
# source -- http://codingbat.com/python/Warmup-2

#----------------------------------------------------------------------

## string_times 
'''
Given a string and a non-negative int n, return a larger string that is
n copies of the original string.
'''
def string_times(str, n):
    return str * n


#----------------------------------------------------------------------

## front_times 
"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""
# My original solution
def front_times(str, n):
    if 0 < len(str) < 3:
        return str * n
    else:
        return str[0:3] * n
# It looks like the solution code set the string length to a variable.
# I can see why: if you need to change the number of chars to multiply,
# you only have to find one line of code to change.


# My later, more concise solution
def front_times(str, n):
    return str[:3] * n


#----------------------------------------------------------------------

## string_bits 
"""
Given a string, return a new string made of every other char starting with
the first, so 'Hello' yields 'Hlo'.
  string_bits('Hi') → 'H'
  string_bits('Heeololeo') → 'Hello'
"""
def string_bits(str):
    return str[0::2]


#----------------------------------------------------------------------

## string_splosion 
"""
Given a non-empty string like 'Code' return a string like 'CCoCodCode'.
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
def string_splosion(str):
    '''Fill a new string with cumulative substrings of the original'''
    splostring = ""
    for i in range(len(str)+1):
        # Concatenate a slice of str from 1st char to i-th char.
        splostring += str[:i] 
    return splostring


#----------------------------------------------------------------------

## last2 
"""
Given a string, return a count of the number of times that a substring of
length 2 appears in the string and is also as the last 2 chars of the string, 
so 'hixxxhi' yields 1 (we won't count the end substring).
last2('xaxxaxaxx') → 1
last2('13121312') → 1
last2('xxxx') → 2
last2('hi') → 0
"""
def last2(str):
    # An end string of length=2 is the search term
    end2 = str[-2:]  
    # Set the remaining string to be searched, initialized with last
    # character removed in order to avoid counting the end substring.
    subst = str[:-1]
    counter = 0
    # As long as we have at least 2 chars remaining in the string to be 
    # searched, slice through it and count the occurences of end2.
    while len(subst) > 1:
        if end2 in subst:
            counter += 1
            # Discard chars prior to the most-recently-found location of end2
            i = subst.find(end2)
            subst = subst[i+1:]
        else:
            break
    return counter


#----------------------------------------------------------------------

## array_count9
"""Given an array of ints, return the number of 9's in the array."""
def array_count9(nums):
    return nums.count(9)


#----------------------------------------------------------------------

## array_front9 
"""
Given an array of ints, return True if one of the first 4 elements 
in the array is a 9. The array length may be less than 4.
array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""
# The Pythonic way is much simpler than their solution.
def array_front9(nums):
    return 9 in nums[:3]


#----------------------------------------------------------------------

## array123 
"""
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array.
array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
"""
# My original solution
def array123(nums):
    numsjoin = ''
    for n in nums: numsjoin += str(n)
    return '123' in numsjoin

# My alternative solution
def array123(nums):
    return '123' in ''.join([str(n) for n in nums])


#----------------------------------------------------------------------

## string_match 
"""
Given two strings, a and b, return a count of the times they both contain the
same length 2 substring at the same index location within the string. So,
"xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings
appear in the same place in both strings.
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""
def string_match(a, b):
    '''NOTE: may've peeked at solution? don't remember if I did or not!'''
    matches = 0
    # Don't iterate past the end of the shorter string
    shorter = min(len(a), len(b))
    for i in range(shorter-1):
        asub = a[i]+a[i+1]
        bsub = b[i]+b[i+1]
        if ( asub == bsub ):
            matches += 1 
    return matches






























































