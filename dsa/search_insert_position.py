# Done on 11 July | Time taken - 41 mins
# Approach:
# Use binary search since the array is sorted.
# Keep two pointers, left and right, spanning the search range.
# At each step, check the middle element:
# If it equals the target, return its index.
# If it's smaller, the target must be to the right → move left up.
# If it's bigger, the target must be to the left → move right down.
# If the loop ends without finding the target, left naturally lands on the correct insert position

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left