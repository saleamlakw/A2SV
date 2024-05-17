class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        dp=[[False]*(m+1) for _ in range(n)]+[[True]*(m+1)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if s[i]==t[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=dp[i][j+1]
        return dp[0][0]



        # memo=[[-1]*m for _ in range(n)]
        # def dp(i,j):
        #     if i>=n:
        #         return True
        #     if j>=m:
        #         return False
        #     if memo[i][j]==-1:
        #         if s[i]==t[j]:
        #             memo[i][j]=dp(i+1,j+1)
        #         else:
        #             memo[i][j]=dp(i,j+1)
        #     return memo[i][j]
        # return dp(0,0)