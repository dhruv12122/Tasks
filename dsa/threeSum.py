class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]
            
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
            
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                
                    left += 1
                    right -= 1
        return result
    
# Time taken 34 mins
# Done on 29 Jun
# Approach first approach was to take one element then to find its compliment andd then find 2 such numbers whose sum
# is equal to the compliment of the taken number 
# To find the 2 numbers i have used a 2 pointer approach where i take a left andd a right pointer and then find the numbers
# For easier finding i have first srted the array so that if the sum is greater ill just move the right pointer by one that 
# means the next number will be smalleer so the sum decreases and if the sum is smaller i move the left one for a greater number
# than the current one so the sum increases 

# The time and space complexity are O(n2) and O(1)