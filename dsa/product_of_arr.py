class Solution(object):
    def productExceptSelf(self, nums):
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        answer = []

        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[i])

        return answer        
    

# Time taken - 25 mins done on 29 Jun
# Approach taken - first idea was to make a complete array of all the elements multipled and then divide by  each element in the final arr
# Since division is not allowed we take the second one that is take the array of elements which contains the sultiplication of all elements 
# before the current one and one for all the elements after the current and then final ans is the multiplication of both arrays 
