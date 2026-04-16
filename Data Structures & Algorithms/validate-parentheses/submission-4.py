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
                # this is a closing bracket so 3 cases:
                # 1. there was never an open bracket
                if len(openbrackets) == 0:
                    return False
                # 2. its closing the wrong type
                if char != bracketmap[openbrackets[-1]]:
                    return False
                # 3. its closing the right type!
                else:
                    openbrackets.pop() 

        if len(openbrackets) == 0:
            return True
        else:
            return False
        