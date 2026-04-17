class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = defaultdict(int)
        maxS = 0

        while r < len(s):
            count[s[r]] += 1
            r += 1

            is_replaceable = (sum(count.values()) - max(count.values())) <= k
            if not is_replaceable:
                count[s[l]] -= 1
                l += 1

            #print(count)
            maxS = max(maxS, sum(count.values()))
            
        return maxS
        