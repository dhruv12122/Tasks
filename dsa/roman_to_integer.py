# Done on - 9 July | Time taken - 27 mins
# Approach:
# Map each Roman numeral symbol to its integer value using a dictionary
# Traverse the string from left to right, one character at a time
# For each character, compare its value with the value of the next character
# If the current value is smaller than the next value, it's a subtractive case (like IV, IX) → subtract it from the total
# Otherwise, add it to the total as usual
# Continue until the end of the string and return the accumulated total

class Solution(object):
    def romanToInt(self, s):
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        
        return total      