class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        res = []
        for _s in s:
            res.append(_s[::-1])
        return " ".join(res)
