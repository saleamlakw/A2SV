class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        re=0
        while s and g:
            if s[-1]>=g[-1]:
                g.pop()
                s.pop()
                re+=1
            else:
                g.pop()
        return re
