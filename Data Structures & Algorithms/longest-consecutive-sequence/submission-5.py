class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start 
            if (n - 1) not in numSet: # A set uses a hash table internally, so x in numSet is O(1) on average
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
