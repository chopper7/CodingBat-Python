# Coding Bat / Python / List 2 / "has22"
# URL -- http://codingbat.com/prob/p119308

"""
Given an array of ints, return True if the array contains a 2 next to
a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""

# My original solution
def has22(nums):
    # T/F flag, initialized False because we haven't found anything yet
    found_two = False
    # If list length is 2 and both items are 2's, set flag to True and return
    if len(nums) == 2 and nums[0]==2==nums[1]:
        found_two = True
        return found_two
    # Start at second element of list (avoids index out of range for i-1)
    for n in range(1, len(nums)-1):
        # If int is a 2 AND EITHER the preceding int is 2 OR the
        # next int is 2, set flag to True
        if nums[n]==2 and (nums[i-1]==2 or nums[i+1]==2):
            found_two = True
            # If we find two consecutive 2's, we're done
            break
    return found_two


# My refactored solution, later (much more concise)
def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False
