# Time taken - 27 mins | Done on 4 July
# Approach:
# Use two pointers at the beginning and end of the array
# Compare the absolute values at both ends
# Place the larger square at the end of the result array
# Move the pointer whose value was used and decrement the result index
# Repeat until all elements are processed

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution(object):
    def sortedSquares(self, nums):
        left = 0 
        right = len(nums) - 1

        result = [0] * len(nums)
        index = len(result) - 1

        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                result[index] = nums[right] ** 2
                right -= 1
            else:
                result[index] = nums[left] ** 2
                left += 1

            index -= 1
        
        return result