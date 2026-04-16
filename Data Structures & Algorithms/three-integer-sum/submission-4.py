class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        #print(nums)

        for first in range(len(nums) - 2):
            if (first > 0) and (nums[first] == nums[first - 1]):
                continue

            second = first + 1
            third = len(nums) - 1
            while (second < third):
                #print("checking", first, ", ", second, ", and", third)

                triplet = nums[first] + nums[second] + nums[third]
                if (triplet > 0): 
                    #print("need smaller")
                    third -= 1
                elif (triplet < 0):
                    #print("need bigger")
                    second += 1
                else:
                    #print("just right")
                    if [nums[first],nums[second],nums[third]] not in triplets:
                        triplets.append([nums[first],nums[second],nums[third]])
                        #print(triplets)

                    third -= 1
 
        return triplets

        