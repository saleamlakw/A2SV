class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])


        dp=[[float("inf")]*(m+1) for _ in range(n-1)]+[matrix[n-1]+[float("inf")]]
        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                if r==n-1:
                    continue
                if r==0:
                    mi=float("inf")
                    for j in range(m):
                        re=min(matrix[r][j]+dp[r+1][j+1], matrix[r][j]+dp[r+1][j-1] if j-1>=0 else float("inf"),matrix[r][j]+dp[r+1][j])
                        mi=min(mi,re)
                    dp[r][c]= mi
                else:
                    dp[r][c]=min(matrix[r][c]+dp[r+1][c+1] , matrix[r][c]+dp[r+1][c-1] if c-1>=0 else float("inf"),matrix[r][c]+dp[r+1][c])
                    # print(dp)
        return dp[0][0]
        
        # def inbound(r,c):
        #     return 0<=r<n and 0<=c<m
        # memo=[[float(-inf)]*m for _ in range(n)]
        # def dp(r,c):
        #     # print(r,c)
            
        #     if not inbound(r,c):
        #         return float("inf")
        #     if r==n-1:
        #         return matrix[r][c]
        #     if memo[r][c]==float(-inf):
        #         if r==0:
        #             mi=float("inf")
        #             for j in range(m):
        #                 re=min(matrix[r][j]+dp(r+1,j+1), matrix[r][j]+dp(r+1,j-1),matrix[r][j]+dp(r+1,j))
        #                 mi=min(mi,re)
        #             memo[r][c]= mi
        #         else:
        #             memo[r][c]=min(matrix[r][c]+dp(r+1,c+1), matrix[r][c]+dp(r+1,c-1),matrix[r][c]+dp(r+1,c))
        #     return memo[r][c]
        # return (dp(0,0))
            
            