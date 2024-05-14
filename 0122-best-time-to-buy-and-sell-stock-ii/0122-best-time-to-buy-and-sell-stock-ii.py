class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=[[0]*2 for _ in range(len(prices)+1)]
        for i in range(len(prices)-1,-1,-1):
            for j in range(2): 
                profit=0
                if j:
                    profit= max(profit,-prices[i]+memo[i+1][0],memo[i+1][1])
                else:
                    profit= max(profit,prices[i]+memo[i+1][1],memo[i+1][0])
                memo[i][j]=profit
        return(memo[0][1])
        