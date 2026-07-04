# Time taken 15 mins | Done on 4 July
# Approach:
# Simple 2 pointer swapping problem

class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return s