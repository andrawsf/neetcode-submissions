class Solution:
    def isValid(self, s: str) -> bool:
        openbrackets = []
        bracketmap = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for char in s: 
            if char in bracketmap:
                openbrackets.append(char)
                # print(openbrackets)
            if char in bracketmap.values():
                # print(openbrackets[-1], " closes with ", bracketmap[openbrackets[-1]])
                # this is a closing bracket - check if it corresponds to the last open
                if len(openbrackets) == 0:
                    return False
                if char != bracketmap[openbrackets[-1]]:
                    return False
                else:
                    openbrackets.pop() 

        if len(openbrackets) == 0:
            return True
        else:
            return False
        