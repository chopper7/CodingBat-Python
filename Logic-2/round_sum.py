# CodingBat / Python / Logic-2 / "round_sum"
# URL -- http://codingbat.com/prob/p100347

"""
For this problem, we'll round an int value up to the next multiple of 10 if its
rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down
to the previous multiple of 10 if its rightmost digit is less than 5, so 12
rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values.
To avoid code repetition, write a separate helper function `def round10(num)`
and call it 3 times. Write the helper entirely below and at the same indent
level as round_sum().
round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10
round_sum(45, 21, 30) → 100
"""
def round10(num):
  '''
  Get the int's rightmost digit.
  If digit is >= 5, round up; if 0 to 4, round down.
  Return the "rounded" num
  '''  
  if num % 10 >= 5:
    return num + (10 - num % 10)
  else:
    return num - (num % 10)


def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)


'''
My COMMENTS

RE: num + (10 - num % 10)
10 - num % 10 is the difference between num's rightmost digit and any multiple
of 10; adding this diff to num increases num to the next multiple of 10.
E.g., if num=36, then 36+(10-(36%10)) ==> 36+(10-6) ==> 36+4 ==> 40.

RE: num - (num % 10)
Subtracting the rightmost digit from the original num
leaves num with a 0 in the rightmost place. 
E.g., if num=34, then 34-(34%10) ==> 34-4 ==> 30

The instructor's code sets num%10 to a variable first, and I
think that's so that the modulus operation is run only one time.
(And therefore might run quicker than mine, or have a smaller Big(O) ?)
'''
