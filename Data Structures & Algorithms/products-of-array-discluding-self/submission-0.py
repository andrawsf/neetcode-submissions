class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first get the full product
        nums_len = len(nums)
        result = [1] * nums_len
        for index in range(nums_len):
            for subindex in range(nums_len):
                if subindex != index: 
                    #print(index, subindex)
                    result[index] *= nums[subindex]
        
        return result
        
