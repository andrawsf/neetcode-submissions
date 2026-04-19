class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = (r + l) // 2

        while l < r:
            m = (r + l) // 2

            print(f"now check [{l}]:{nums[l]} [{m}]:{nums[m]} [{r}]:{nums[r]}")
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            # is the left sorted?
            if nums[l] < nums[m]:
                # perfect then just check if its in between
                if nums[l] < target < nums[m]:
                    #target is in between left and mid
                    print("sorted: go left")
                    r = m - 1
                else:
                    #target is on right
                    print("sorted: go right")
                    l = m + 1
            else:
                if target < nums[m]:
                    #target is in between left and mid
                    print("unsorted: go left")
                    r = m - 1
                else:
                    #target is on right
                    print("unsorted: go right")
                    l = m + 1

        if target == nums[l]:
            return l
        elif target == nums[r]:
            return r
        elif m and target == nums[m]:
            return m
        else:
            return -1