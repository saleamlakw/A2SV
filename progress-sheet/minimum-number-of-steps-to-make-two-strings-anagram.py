class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs=Counter(s)
        ct=Counter(t)
        re=0
        for i in ct:
            if i in cs:
                if cs[i]>=ct[i]:
                    re+=ct[i]
                else:
                    re+=cs[i]
                
        return len(t)-re

