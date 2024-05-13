class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo={}
        def dp(i,t):
            if i>=len(days):
                return 0
            if (i,t) not in memo:
                re=float("inf")
                if days[i]>=t:
                    re=min(dp(i+1,days[i]+1)+costs[0],dp(i+1,days[i]+7)+costs[1],dp(i+1,days[i]+30)+costs[2])
                else:
                    re=min(re,dp(i+1,t))
                memo[(i,t)]=re
            return memo[(i,t)]
        return dp(0,0)
            
