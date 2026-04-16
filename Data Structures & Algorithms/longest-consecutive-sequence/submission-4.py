class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_sequence = 1
        curr_sequence = 1 
        #print(nums)
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            #print("cmpar ", nums[i], " and ", nums[i-1])
            #print(nums[i]-1, " and ", nums[i-1])
            if nums[i] == nums[i-1]:
                continue
            if nums[i]-1 == nums[i-1]:
                curr_sequence += 1
                #print(curr_sequence, " growing")
            else:
                curr_sequence = 1
                #print("resetting")
            if curr_sequence > max_sequence:
                max_sequence = curr_sequence
        
        return max_sequence