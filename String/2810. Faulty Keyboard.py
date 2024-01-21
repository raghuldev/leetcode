class Solution:
    def finalString(self, s: str) -> str:
        new_str = ""
        for letter in s:
            if letter == "i":
                new_str = new_str[::-1]
                continue
            new_str += letter
        return new_str