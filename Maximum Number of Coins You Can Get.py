class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        re=0
        piles.sort()
        while piles:
            piles.pop()
            re+=piles.pop()
            piles.pop(0)
        return re

