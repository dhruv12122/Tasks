# Time taken 15 mins, done on 2 July
# Approach: the simple idea was to initiate 2 pointers left and right at first index
# For the right pointer if the element is 0 then move it foreward
# For the left pointer if the right is 0 and left is a number swap them
# Continue this loop and eventually the zeros will be atthe end

# Code
class Solution(object):
    def moveZeroes(self, nums):
        left, right = 0, 0

        while right < len(nums):
            if nums[right] == 0:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
