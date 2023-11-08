class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        co=Counter()
        re=0
        for r in range(len(s)):
            co[s[r]]+=1
            while ((r-l+1)-max(co.values())>k):
                co[s[l]]-=1
                l+=1
            re=max(re,r-l+1)
        return re
            