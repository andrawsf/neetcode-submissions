class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map_of_maps = dict()

        for string in strs:
            map = dict()
            for char in string:
                if char in map:
                    map[char] += 1
                else:
                    map[char] = 1
            #print(map.items())
            if frozenset(map.items()) in map_of_maps:
                map_of_maps[frozenset(map.items())].append(string)
            else:
                map_of_maps[frozenset(map.items())] = [string]
            #print(map_of_maps)
        
        print(list(map_of_maps.values()))
        return list(map_of_maps.values())

        