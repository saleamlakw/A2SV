class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #dp with space optimization

        pre=[0]*(max(days)+31)
        cur=[0]*(max(days)+31)
        for i in range(len(days)-1,-1,-1):
            for pass_days in range(max(days),-1,-1):
                if days[i]>pass_days:
                    take=min(costs[0]+pre[days[i]],costs[1]+pre[days[i]+6],costs[2]+pre[days[i]+29])
                    cur[pass_days]=take
                else:   
                    nottake=pre[pass_days]
                    cur[pass_days]=nottake
            pre=cur[:]
            cur=[0]*(max(days)+31)
        return pre[0]
        
        #tabulation 

        # dp=[[0]*(max(days)+31) for _ in range(len(days)+1)]
        # for i in range(len(days)-1,-1,-1):
        #     for pass_days in range(max(days),-1,-1):
        #         if days[i]>pass_days:
        #             take=min(costs[0]+dp[i+1][days[i]],costs[1]+dp[i+1][days[i]+6],costs[2]+dp[i+1][days[i]+29])
        #             dp[i][pass_days]=take
        #         else:   
        #             nottake=dp[i+1][pass_days]
        #             dp[i][pass_days]=nottake
        # return dp[0][0]

        #memoization

        # memo=Counter()
        # def dp(i,pass_days):
        #     if i>=len(days):
        #         return 0
        #     if (i,pass_days) not in memo:
        #         if days[i]>pass_days:
        #             take=min(costs[0]+dp(i+1,days[i]),costs[1]+dp(i+1,days[i]+6),costs[2]+dp(i+1,days[i]+29))
        #             memo[(i,pass_days)]=take
        #         else:   
        #             nottake=dp(i+1,pass_days)
        #             memo[(i,pass_days)]=nottake
        #     return memo[(i,pass_days)]
        # return dp(0,0)
