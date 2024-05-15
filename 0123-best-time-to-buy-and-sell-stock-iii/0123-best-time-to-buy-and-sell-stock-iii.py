class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dp(i,state,idx):
            if idx>1:
                return 0

            if i>=len(prices):
                return 0
            if (i,state,idx) not in memo:
                re=0
                if state:
                    re=max(-prices[i]+dp(i+1,0,idx),dp(i+1,1,idx))
                else:
                    re=max(prices[i]+dp(i+1,1,idx+1),dp(i+1,0,idx))
                memo[(i,state,idx)]=re
            return memo[(i,state,idx)]
        return dp(0,1,0)


