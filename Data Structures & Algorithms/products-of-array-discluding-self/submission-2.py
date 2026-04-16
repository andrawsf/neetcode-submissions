class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first get the full product
        nums_len = len(nums)
        result = [1] * nums_len
        product = 1
        zero_cnt = 0
        for index in range(nums_len):
            if nums[index] != 0:
                product *= nums[index]
            else: 
                zero_cnt += 1
        
        for index in range(nums_len):
            if zero_cnt > 1:
                return [0] * nums_len
            elif zero_cnt == 0:
                result[index] = (int)(product/nums[index])
            else:
                if nums[index] != 0:
                    result[index] = 0
                else:
                    result[index] = (int)(product)
        
        return result
        
