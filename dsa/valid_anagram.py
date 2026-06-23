class Solution(object):
    def isAnagram(self, s, t):
        s_map = {}
        t_map = {}

        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1
        
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1
        
        return s_map == t_map