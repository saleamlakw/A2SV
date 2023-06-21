class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s)!=len(t):
            return False
        a=dict(Counter(s))
        for i in a:
            if a[i]!=t.count(i):
                return False
        return True
