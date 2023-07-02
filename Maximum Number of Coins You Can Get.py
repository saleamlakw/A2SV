class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        re=0
        i=0
        while i<len(piles):
            a=piles[i]
            re+=piles[i+1]
            b=piles.pop()
            i+=2
        return re

