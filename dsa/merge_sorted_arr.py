# Done on 11 July | Time taken - 34 mins
# Approach:
# Fill nums1 from the back instead of the front, since it has extra empty space at the end (avoids overwriting unmerged elements).
# Use three pointers: i (last real element in nums1), j (last element in nums2), k (last index of the merged array).
# Compare nums1[i] and nums2[j], place the larger one at nums1[k], then move that pointer and k backward.
# Stop once j < 0 — meaning all of nums2 is merged in (leftover elements in nums1 are already in place, so no need to copy them).


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1        
        k = m + n - 1     
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1