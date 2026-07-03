# Time taken - 40 mins | done on 3 July
# Approach :
# Use Binary Search since the required time complexity is O(log n)
# In every iteration, find the middle element 
# Check which half of the array is sorted 
# If the target lies in the sorted half, search that half 
# Otherwise, search the other half 
# If the target is found, return its index; otherwise return -1 


class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1