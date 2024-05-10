class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_=float("inf")
        max_=0

        for ele in prices:
            min_=min(min_,ele)
            max_=max(max_,ele-min_)
        return max_