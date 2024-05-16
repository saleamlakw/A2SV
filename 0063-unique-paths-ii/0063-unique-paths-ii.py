class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo=Counter()
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[0]*m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if r==0 and c==0 and obstacleGrid[r][c]!=1:
                    dp[0][0]=1
                    continue
                if obstacleGrid[r][c]!=1:
                    up=dp[r-1][c] if r-1>=0 else 0
                    left=dp[r][c-1] if c-1 >=0 else 0
                    dp[r][c]=up+left
        print(dp)
        return dp[n-1][m-1]


        def inbound(r,c):
            return 0<=r<n and 0<=c<m
        def dp(r,c):
            if not inbound(r,c) or obstacleGrid[r][c]==1:
                return 0
            if r==0 and c==0:
                return 1
            if (r,c) not in memo:
                up=dp(r-1,c)
                left=dp(r,c-1)
                memo[(r,c)]=up+left
            return memo[(r,c)]
        return dp(n-1,m-1)