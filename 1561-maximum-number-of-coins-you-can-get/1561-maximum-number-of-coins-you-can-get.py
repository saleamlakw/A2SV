class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        re=0
        l=0
        r=len(piles)-1
        while l<r:
            r-=1
            re+=piles[r]
            r-=1
            l+=1
        return re
            