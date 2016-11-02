# Coding Bat / Python / List 1 / "rotate_left3"
# URL -- http://codingbat.com/prob/p148661

"""
Given an array of ints length 3, return an array with the elements 
"rotated left" -- so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""

def rotate_left3(nums):
    # split it up
    left = nums[0]
    rotated = nums[1:]
    # rearrange it
    rotated.append(left)
    return rotated
