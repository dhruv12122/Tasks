# Time taken - 15 mins | done on 3 July
# Approach:
# The list is sortedd and we have to use binary search in O(LogN)
# Do a simple binary search code for this 

class Solution(object):
    def search(self, nums, target):
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
        
        return -1