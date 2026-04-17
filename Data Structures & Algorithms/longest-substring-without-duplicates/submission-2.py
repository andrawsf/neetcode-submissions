class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxStringLen = 0

        while r < len(s):
            #print(s[l:r])
            if s[r] in s[l:r]:
                l += 1
            else:
                r += 1
            currMax = r - l
            maxStringLen = max(maxStringLen, currMax)

        return maxStringLen