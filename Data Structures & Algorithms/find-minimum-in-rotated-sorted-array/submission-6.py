class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[l]

        while l < r:
            m = (r + l) // 2

            #print(f"now check [{l}]:{nums[l]} [{m}]:{nums[m]} [{r}]:{nums[r]}")
            minimum = min(minimum,nums[m])
            if nums[l] <= nums[m] <= nums[r]:
                #all sorted - return
                return min(nums[l],minimum)
            elif nums[l] <= nums[m]:
                #left side is sorted - go right
                minimum = min(nums[r],minimum)
                #print("go right")
                l = m + 1
            else:
                #right is sorted - go left
                minimum = min(nums[l],minimum)
                #print("go left")
                r = m - 1
    
        return minimum
