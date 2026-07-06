# Time taken - 52 mins | Done on 6 July
# Approach:
# Here first we take a window and keep expanding it till we hit a zero
# When we hit the zero we increase the zero counter by 1
# When the zero count is greater than k we shrink the window from left till the zero count is equal to k
# Along with this we keep the max length too and at the end we return it

class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        
        return max_length