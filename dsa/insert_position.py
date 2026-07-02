# Time taken - 29 mins   done on 2 July
# Approach:
# Since the array is sorted, use Binary Search to achieve O(log n)
# Find the middle element
# If nums[mid] == target, return mid
# If nums[mid] < target, search the right half
# If nums[mid] > target, search the left half
# If the target is not found, return 'left' because it points to the correct insertion index

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
