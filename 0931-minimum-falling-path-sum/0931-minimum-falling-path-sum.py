class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        def inbound(r,c):
            return 0<=r<n and 0<=c<m
        memo={}
        def dp(r,c):
            # print(r,c)
            if not inbound(r,c):
                return float("inf")
            if r==n-1:
                return matrix[r][c]
            if (r,c)not in memo:
                if r==0:
                    mi=float("inf")
                    for j in range(m):
                        re=min(matrix[r][j]+dp(r+1,j+1), matrix[r][j]+dp(r+1,j-1),matrix[r][j]+dp(r+1,j))
                        mi=min(mi,re)
                    memo[(r,c)]= mi
                else:
                    memo[(r,c)]=min(matrix[r][c]+dp(r+1,c+1), matrix[r][c]+dp(r+1,c-1),matrix[r][c]+dp(r+1,c))
            return memo[(r,c)]
        return (dp(0,0))
            
            