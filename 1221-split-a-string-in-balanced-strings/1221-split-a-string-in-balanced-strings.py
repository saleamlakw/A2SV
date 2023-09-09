class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r=0
        l=0
        re=0
        for i in s:
            if i=="L":
                l+=1
            else:
                r+=1
            if l==r:
                re+=1
        return re
        