# Coding Bat / Python / String-2 / "count_hi"
# URL -- http://codingbat.com/prob/p167246

"""
Return the number of times that the string 'hi' appears anywhere in the
given string.
count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""

def count_hi(str):
  # "hi" has length of 2, so we're looking at substrings of len 2
  count = 0
  for i in range(len(str)-1):
    if str[i:(i+2)] == 'hi':
      count += 1
  return count