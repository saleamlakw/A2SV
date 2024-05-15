class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp=[[[0,0,0] for _ in range(2)]for _ in range(len(prices)+1)]
        for i in range(len(prices)-1,-1,-1):
            for j in range(2):
                for k in range(2):
                    re=0
                    if j:
                        re=max(-prices[i]+dp[i+1][0][k],dp[i+1][1][k])
                    else:
                        re=max(prices[i]+dp[i+1][1][k+1],dp[i+1][0][k])
                    dp[i][j][k]=re
        return dp[0][1][0]
        

