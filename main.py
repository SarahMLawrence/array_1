"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
  # UPER
  # UNDERSTAND
  # - don't include the actual index in either of the sums
  # - Would a single number return itself or -1? Lets assume -1

  # PLAN:
  # default return variable is -1
  # if nums is empty or size 1, return -1

  # left = 0
  # right = sum of entire array
  # iterate through the array
  #   add nums[i] to left_side_sum
  #   rigt side = sum of the entire array - left- nums
  #

  # The most straightforward:
  # iterate through
  # for each index, sum up the left side and right side and compare

  if len(nums) <= 1:
    return -1
  left = 0
  right = sum(nums)

  for i in range(len(nums)):
      right -=nums[i]
      if left == right:
          return i

      left += nums[i]

  return -1

print(pivot_index([1, 7, 3, 6, 5, 6]))
