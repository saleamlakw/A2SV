class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        re=0
        for r in costs:
            if coins-r>=0:
                coins-=r
                re+=1
        return re
