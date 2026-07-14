# Time taken - 32 mins | Done on 14 July
# Approach:
# Use a HashMap where the key is the sorted version of each string.
# Traverse the list of strings and sort each string to create a common key.
# If the key is not present, create a new list.
# Append the original string to its corresponding group.
# Return all grouped anagrams.

class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            key = tuple(sorted(s))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)
            
        return list(groups.values())
            