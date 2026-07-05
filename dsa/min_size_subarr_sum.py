# Time taken - 47 mins | Done on 5 July
# Approach:
# Use a sliding window with two pointers.
# Expand the window by moving the right pointer and keep adding elements to the current sum.
# Once the sum becomes greater than or equal to the target, update the minimum length.
# Shrink the window from the left while the condition is still satisfied.
# Repeat until the entire array is processed.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        seen = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])

            max_length = max(max_length, right - left + 1)
        
        return max_length