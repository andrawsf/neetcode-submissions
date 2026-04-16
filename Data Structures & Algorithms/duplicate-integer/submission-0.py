class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = dict()
        for number in nums:
            if number in visited:
                return True
            else:
                visited[number] = True
        return False