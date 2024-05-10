class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=Counter()
        def dp(i,state):
            if i>=len(prices):
                return 0
            profit=float("-inf")
            if (i,state) not in memo:
                if state:
                    buy=-prices[i]+dp(i+1,0)
                    notbuy=dp(i+1,1)
                    memo[(i,state)]=max([profit,buy,notbuy])
                else:
                    sell=prices[i]+dp(i+1,1)
                    notsell=dp(i+1,0)
                    memo[(i,state)]=max([profit,sell,notsell])
            return memo[(i,state)]
        return dp(0,1)
        