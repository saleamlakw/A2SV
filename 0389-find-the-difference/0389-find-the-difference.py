class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss=Counter(s)
        tt=Counter(t)
        for i in t:
            if i not in ss:
                return i
            elif ss[i]!=tt[i]:
                return i