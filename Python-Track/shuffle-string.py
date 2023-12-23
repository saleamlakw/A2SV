class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        li=[0]*len(s)
        for r in range(len(s)):
            li[indices[r]]=s[r]
        return "".join(li)