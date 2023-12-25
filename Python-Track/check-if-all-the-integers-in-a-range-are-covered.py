class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        a=set()
        for r in ranges:
            for i in range(r[0],r[1]+1):
                a.add(i)
        # print(a)
        b=set()
        for l in range(left,right+1):
            b.add(l)
        # print(b)
        return b.issubset(a)
        