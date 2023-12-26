class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        for r in range(0,len(s),2*k):
            s[r:r+k]=s[r:r+k][::-1]
        return "".join(s)