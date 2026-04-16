class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map_of_maps = defaultdict(list)

        for string in strs:
            map = defaultdict(int)
            for char in string:
                map[char] += 1
            
            map_of_maps[frozenset(map.items())].append(string)
        
        #print(list(map_of_maps.values()))
        return list(map_of_maps.values())

        