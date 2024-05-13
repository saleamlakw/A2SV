class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo=Counter() #--->o(n)+2*o(n)
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        print(dp)

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                up=dp[i-1][j] if i>0 else 0
                left=dp[i][j-1] if j>0 else 0
                dp[i][j]=up+left
        return dp[m-1][n-1]
       
            