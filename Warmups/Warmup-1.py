# Coding Bat / Python / Warmup-1
# All problems from this section are included in this script.
# source -- http://codingbat.com/python/Warmup-1

#----------------------------------------------------------------------

## sleep_in
''' The parameter weekday is True if it is a weekday, and the parameter vacation 
is True if we are on vacation. We sleep in if it is not a weekday or we're on
vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''
# original solution, 2015
def sleep_in(weekday, vacation):
    return weekday == False or vacation == True

# Refactored solution, 2016:
def sleep_in(weekday, vacation):
    return vacation or not weekday


#----------------------------------------------------------------------

## monkey_trouble
''' 
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


#----------------------------------------------------------------------

## sum_double 
'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


#----------------------------------------------------------------------

## diff21 
'''
Given an int n, return the absolute difference between n and 21, except return 
double the absolute difference if n is over 21. [Can be solved without calling
the abs() function.]
diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''
# original solution
def diff21(n):
  if n <= 21:
      return abs(n-21)
  else:
      return 2*abs(n-21)

# Alternately, without calling abs()
def diff21(n):
    if n > 21:
        diff = 2 * (n - 21)
    else:
        diff = -(n - 21)
    return diff


#----------------------------------------------------------------------

## parrot_trouble
'''
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
'''
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


#----------------------------------------------------------------------

## makes10 
'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
'''
def makes10(a, b):
  return (10 in (a,b)) or (a + b == 10)


#----------------------------------------------------------------------

## near_hundred 
'''Given an int n, return True if it is within 10 of 100 or 200.'''
def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


#----------------------------------------------------------------------

## pos_neg 
'''
Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return True only if both 
are negative.
'''
def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else:
    return (a < 0 < b) or (b < 0 < a)


#----------------------------------------------------------------------

## not_string 
'''
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.
'''
def not_string(str):
  if str.startswith('not'):
    return str
  else:
    return 'not ' + str


#----------------------------------------------------------------------

## missing_char 
'''
Given a non-empty string and an int n, return a new string where the char at
index n has been removed. The value of n will be a valid index of a char in
the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
'''
# My original solution
def missing_char(str, n):
    return str[0:n] + str[n+1:]

# Alternative solution
def missing_char(str, n):
    return str.replace(str[n], '')


#----------------------------------------------------------------------

## front_back 
'''
Given a string, return a new string where the first and last chars have been
exchanged.
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''
def front_back(str):
  if len(str) > 1:
    return str[-1] + str[1:-1] + str[0]
  else:
    return str


#----------------------------------------------------------------------

## front3 
'''
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
front3('Java') → 'JavJavJav'
'''
def front3(str):
    return str[:3] * 3
