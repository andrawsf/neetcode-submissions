class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += string + "ç"
            #print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        prev_index = 0
        for index in range(len(s)):
            if s[index] == "ç":
                decoded.append(s[prev_index:index])
                prev_index = index + 1
        return decoded
