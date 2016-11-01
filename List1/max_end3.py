# Coding Bat / Python / List 1 / "max_end3"
# URL -- http://codingbat.com/prob/p135290
 
"""
Given an array of ints length 3, figure out which is the larger of the first
and last elements in the array, and set all the elements to be that value. 
Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([0, 0, 1]) → [1, 1, 1]
"""

# My original solution, 2015
def max_end3(nums):
    largest = max(nums[0::-1])
    for i in range(len(nums)):
        nums[i] = largest
    return nums

# My refactored solution, 2016
def max_end3(nums):
    largest = max(nums[0::-1])
    return [largest] * len(nums)