class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r,c=len(matrix),len(matrix[0])
        dp=[[0]*c for _ in range(r)]
        result=0
        for i in range(r):
            for j in range(c):
                if matrix[i][j]=="1":
                        re=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) if i>0 and j>0 else 0
                        dp[i][j]=1+re
                        result=max(result,dp[i][j])
        return result*result
