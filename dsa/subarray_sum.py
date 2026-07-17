# Done on 17 July | Time taken - 44 mins

# Approach:
# Track the running prefix_sum as you iterate through the array.
# The key insight: if prefix_sum - k has occurred before, it means the subarray between that earlier point and now sums to exactly k.
# Use a hashmap sum_freq to store how many times each prefix sum has occurred.
# Initialize sum_freq = {0: 1} to handle subarrays that start from index 0.
# For each number, update prefix_sum, check if prefix_sum - k exists in the map (add its frequency to count), then record the current prefix_sum in the map.

class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        sum_freq = {0: 1}
        
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in sum_freq:
                count += sum_freq[prefix_sum - k]
            sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
        
        return count