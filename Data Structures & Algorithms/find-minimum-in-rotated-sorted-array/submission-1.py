class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        middle = (int)(len(nums) / 2)
        print(middle)

        # we will always find smth eventually - no risk
        while True:
            first = nums[(middle - 1) % len(nums)]
            second = nums[middle % len(nums)]
            third = nums[(middle + 1) % len(nums)]
            #print("comp ", first,",",second,",",third)
            if first < second < third:
                # sorted - go down
                middle -= 1
            else: 
                return min(first, second, third)
