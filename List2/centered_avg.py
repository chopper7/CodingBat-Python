# Coding Bat / Python / List 2 / "centered_average"
# URL -- http://codingbat.com/prob/p126968
 
"""
Original problem statement:

Return the "centered" average of an array of ints, which we'll say is
the mean average of the values, except ignoring the largest and smallest
values in the array. If there are multiple copies of the smallest value,
ignore just one copy, and likewise for the largest value. Use int division
to produce the final average. You may assume that the array is length 3
or more.

Examples:
centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""

# My original solution
def centered_average(nums):
  nsort = sorted(nums)[1:-1]
  sum = 0
  for n in nsort:
    sum += n
  return sum / len(nsort)


# Refactored, a year later
def centered_average(nums):
    small_to_large = nums.sort()
    middle_nums = small_to_large[1:-1]
    return sum(middle_nums) / len(middle_nums)


# Another refactored solution
def centered_average(nums):
    middle_nums = sorted(nums)[1:-1]
    return sum(middle_nums) / len(middle_nums)

