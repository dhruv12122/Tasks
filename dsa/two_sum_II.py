# Done on - 17 July | Time taken 29 mins
#Approach:
# Since the array is sorted, use two pointers — one at the start (left), one at the end (right).
# If the sum of the two pointed values equals the target, return their (1-indexed) positions.
# If the sum is too small, move left right to increase the sum.
# If the sum is too big, move right left to decrease the sum.

class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        
        return []