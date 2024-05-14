class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=[[-1]*2 for _ in range(len(prices))]
        def dp(i,state):
            if i>=len(prices):
                return 0
            if memo[i][state]==-1:
                profit=float("-inf")
                if state:
                    profit= max(profit,-prices[i]+dp(i+1,0),dp(i+1,1))
                else:
                    profit= max(profit,prices[i]+dp(i+1,1),dp(i+1,0))
                memo[i][state]=profit
            return memo[i][state]
        return dp(0,1)