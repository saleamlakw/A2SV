class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=[[-1]*2 for _ in range(len(prices))]
        def dp(i,state):
            if i>=len(prices):
                return 0
            if memo[i][state]==-1:
                profit=float("-inf")
                if state:
                    take=-prices[i]+dp(i+1,0)
                    nottake=dp(i+1,1)
                    profit= max(profit,max(take,nottake))
                else:
                    take=prices[i]+dp(i+1,1)
                    nottake=dp(i+1,0)
                    profit= max(profit,max(take,nottake))
                memo[i][state]=profit
            return memo[i][state]
        return dp(0,1)