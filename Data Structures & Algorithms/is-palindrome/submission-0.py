class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1

        while back > front:
            #print("Comparing ", s[back], " and ", s[front])
            if not s[back].isalnum():
                #print("Inc back")
                back -= 1
            elif not s[front].isalnum():
                #print("Inc front")
                front += 1
            elif s[back].lower() != s[front].lower():
                #print("FAILED")
                return False
            else:
                #print("MATCHED!")
                back -= 1
                front += 1
        return True
        