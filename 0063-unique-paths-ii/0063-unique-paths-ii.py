class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo=Counter()
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])

        dp=[[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i==0 and j==0 and obstacleGrid[i][j]!=1:
                    dp[i][j]=1
                else:
                    
                    up,left=0,0
                    if obstacleGrid[i][j]!=1:
                        if i-1>=0 and obstacleGrid[i-1][j]!=1:
                            up=dp[i-1][j]
                        if j-1>=0 and obstacleGrid[i][j-1]!=1:
                            left=dp[i][j-1]
                    dp[i][j]=up+left

        return dp[n-1][m-1]
        # def inbound(r,c):
        #     return 0<=r<n and 0<=c<m
        # def dp(r,c):
        #     if not inbound(r,c) or obstacleGrid[r][c]==1:
        #         return 0
        #     if r==0 and c==0:
        #         return 1
        #     if (r,c) not in memo:
        #         up=dp(r-1,c)
        #         left=dp(r,c-1)
        #         memo[(r,c)]=up+left
        #     return memo[(r,c)]
        # return dp(n-1,m-1)