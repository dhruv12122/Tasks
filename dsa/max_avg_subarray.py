# Time taken - 23 mins | Done  on 6 July
# Approach:
# Since we have a fixed window we take first k elements in the window and get the sum
# Then compare the sum with max sum and update max sum 
# Then the next element is added to sum and first element is removed from the sum
# Lastly for the max sum we average it by dividing with k and then return it

class Solution(object):
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for right in range(k, len(nums)):
            current_sum += nums[right]
            current_sum -= nums[right - k]

            max_sum = max(max_sum, current_sum)
        
        return max_sum / float(k)