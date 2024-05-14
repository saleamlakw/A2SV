class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_=float("inf")
        result=0
        for i in range(len(prices)):
            result=max(result,prices[i]-min_)
            min_=min(min_,prices[i])
        return result
