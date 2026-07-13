# Done on 12 July | time taken 22 mins
# Approach:
# Use two pointers: read and write
# Traverse the array using the read pointer
# If the current element is not equal to val, copy it to the write pointer
# Move the write pointer only after copying a valid element
# Continue until the end of the array and return write as the new length

class Solution(object):
    def removeElement(self, nums, val):
        read = 0
        write = 0

        while read < len(nums):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

            read += 1

        return write