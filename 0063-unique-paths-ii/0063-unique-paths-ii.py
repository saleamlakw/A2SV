class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo=Counter()
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
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