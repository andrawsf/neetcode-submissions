class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        referenceMap, windowMap = defaultdict(int), defaultdict(int)
        substr = ""

        # first map out t
        for c in t:
            referenceMap[c] += 1
        print(referenceMap)

        while r < len(s):
            windowMap[s[r]] += 1
            #print("checking l=",l,"r=",r, s[l:r+1])
            while self.isMapInMap(windowMap, referenceMap):
                #print("In substr loop: ", s[l:r+1])
                if substr == "" or len(substr) > len(s[l:r+1]):
                    #print("setting as new winner!")
                    substr = s[l:r+1]
                windowMap[s[l]] -= 1
                l += 1 # keep looking for smaller
            r += 1
            
        return substr

    def isMapInMap(self, s: dict[int], t: dict[int]) -> bool:
        for key in t:
            print("for key=", key, " s[key]=",s[key]," t[key]=",t[key],)
            if s[key] < t[key]:
                print("return false")
                return False
        return True



        