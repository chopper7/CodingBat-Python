# Coding Bat / Python / List 2 / "sum13"
# URL -- http://codingbat.com/prob/p167025

"""
Original challenge:
Return the sum of the numbers in the array, returning 0 for an empty array.
...the number 13 is very unlucky, so it does not count
and numbers that come immediately after a 13 also do not count.
E.g.,
sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""

#-----------------------------------------------------------------------

# My solution to original challenge

def sum13(nums):
    if 13 not in nums:
        return sum(nums)
    total = 0
    # If first item is not 13, add it to sum
    if nums[0] != 13:
        total += nums[0]
    # For the rest of the list, test whether each number and the number
    # preceding it is 13. If neither is 13, add the current number to sum.
    for i in range(1, len(nums)):
      if nums[i] != 13 and nums[i-1] != 13:
          total += nums[i]  
    return total


#-----------------------------------------------------------------------


# Later, I refactored it to accept any number (not just 13) as the
# "exception" number.

def sum_excluding(nums, n):
    # If n is not in list, just return sum of list
    if n not in nums:
        return sum(nums)
    
    total = 0
    # If first item is not n, add it to total.
    if nums[0] != n:
        total += nums[0]
        
    # For the rest of the list, test whether current number and the number
    # preceding it is n. If neither is n, add current number to total.
    for i in range(1, len(nums)):
        if nums[i] != n and nums[i-1] != n:
            total += nums[i]

    return total


# Just run the refactored function, to demonstrate it
print(sum_excluding([1, 2, 2, 1, 13], 13))
