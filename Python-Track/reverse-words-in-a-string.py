class Solution:
    def reverseWords(self, s: str) -> str:
        r=s.split()
        r.reverse()
        return " ".join(r)   