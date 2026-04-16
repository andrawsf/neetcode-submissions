class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dont even bother if len is dif
        if len(s) != len(t):
            return False

        s_map = dict()
        t_map = dict()
        size = len(s)
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

        #print(s_map)
        #print(t_map)
        if s_map == t_map:
            return True
        
        return False