# Coding Bat / Python / List 2 / "sum67"
# URL -- http://codingbat.com/prob/p108886

"""
Return the sum of the numbers in the array, except ignore sections of
numbers starting with a 6 and extending to the next 7 (every 6 will be
followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""


# My solution

def sum67(nums):
    ranges67 = []
    for i in range(len(nums)-1):
        if nums[i] == 6:
            idx6 = nums[i:].index(6)
            idx7 = nums[i:].index(7)
            ranges67.append((idx6+i, idx7+i))
    for r in ranges67:
        for i in range(r[0], r[1]+1):
            nums[i] = 0
    return sum(nums)

"""
My Solution -- Explanation:

Find any and all ranges of 6 to 7 in list, save their indexes, then use
those indexes as a slice of the list. Set to 0 all values in within that
slice.
    1) Iterate through the list until the next-to-last item.
    2) If you find a 6,
       --Get the start and stop indices of that 6-to-7 slice in the list,
         and save them as a tuple in the `ranges67` list.
       --Append to ranges67 each tuple of 6 and 7 indices found.
    3) For each tuple of indices in the ranges67 list,
       --Use the tuple's two values to as a range of indices,
       --with which to set to 0 the value at each corresponding index of nums.
    4) Sum up the remaining values of the nums list
"""
