class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        result = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_freq = sorted(freq.items(), key = lambda x:x[1], reverse = True)

        for num, count in sorted_freq[:k]:
            result.append(num)
        
        return result
