class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=Counter()
        def dp(i,state):
            if i>=len(prices):
                return 0
            profit=float("-inf")
            if (i,state) not in memo:
                if state:
                    memo[(i,state)]=max(-prices[i]+dp(i+1,0),dp(i+1,1))
                else:
                    memo[(i,state)]=max(prices[i]+dp(i+2,1),dp(i+1,0))
            return memo[(i,state)]
        return dp(0,1)