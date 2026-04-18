class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        referenceMap, windowMap = defaultdict(int), defaultdict(int)
        substr = ""
        referenceSize, windowSize = 0, 0

        # first map out t
        for c in t:
            referenceMap[c] += 1
        referenceSize = len(referenceMap)
        #print(referenceMap)

        while r < len(s):
            windowMap[s[r]] += 1
            #print("checking l=",l,"r=",r, s[l:r+1])
            if windowMap[s[r]] == referenceMap[s[r]]:
                windowSize += 1
            while windowSize == referenceSize:
                #print("In substr loop: ", s[l:r+1])
                if substr == "" or len(substr) > len(s[l:r+1]):
                    #print("setting as new winner!")
                    substr = s[l:r+1]
                windowMap[s[l]] -= 1
                if windowMap[s[l]] < referenceMap[s[l]]:
                    windowSize -= 1
                l += 1 # keep looking for smaller
            r += 1
            
        return substr



        