class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # this one we will use bucket sort but with counts as the bucket
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        for c in range(len(freq) - 1, 0, -1):
            for high_num in freq[c]:
                result.append(high_num)
                if len(result) == k:
                    return result

        