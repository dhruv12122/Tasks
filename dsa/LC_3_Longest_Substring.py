# Time taken - 50 mins | Done on 5 July
# Approach:
# Use a sliding window with two pointers and a set to store unique characters.
# Expand the window by moving the right pointer.
# If a duplicate character is found, keep shrinking the window from the left until it becomes valid.
# Add the current character to the set and update the maximum window length.
# Continue until all characters are processed.

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
