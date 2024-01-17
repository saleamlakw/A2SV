class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l=0
        r=len(piles)-1
        k=len(piles)-2
        re=0
        while l<k:
            re+=piles[k]
            k-=2
            l+=1
        return re
