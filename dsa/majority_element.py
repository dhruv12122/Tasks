# Done on 13 July | Timme taken - 20 mins
# Approach:
# Use a HashMap to store the frequency of each element
# Traverse the array and update the count of each number
# As soon as any element's frequency becomes greater than n // 2,
#    return that element


class Solution(object):
    def majorityElement(self, nums):
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums) // 2:
                return num