class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)

        dp=[0]*(n+1)
        dp[n]=-1
        for i in range(n-1,-1,-1):
            re=float("inf")
            st=""
            for j in range(i,n):
                st+=s[j]
                if st==st[::-1]:
                    re=min(re,1+dp[j+1])
            dp[i]=re
            # print(dp)
        return dp[0]
        # memo={}
        # def dp(i):
        #     if i>=n:
        #         return -1
        #     if i not in memo:
        #         re=float("inf")
        #         st=""
        #         for j in range(i,n):
        #             st+=s[j]
        #             if st==st[::-1]:
        #                 re=min(re,1+dp(j+1))
        #         memo[i]=re
        #     return memo[i]
        # return dp(0)
                
