class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create map of frequency
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1
        
        #print(frequency_map)

        # then sort by the freq
        highest_numbers = []
        numbers_found = 0
        while numbers_found < k:
            max_freq = 0
            max_freq_int = None
            for key in frequency_map:
                if frequency_map[key] > max_freq and key not in highest_numbers:
                    max_freq = frequency_map[key]
                    max_freq_int = key
            highest_numbers.append(max_freq_int)
            numbers_found += 1
        return highest_numbers
        