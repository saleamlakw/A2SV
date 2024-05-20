class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row=len(triangle)
        col=len(triangle[-1])
        dp=[[float("inf")]*(col+1) for _ in range(row-1)]+[triangle[-1]+[float("inf")]]
        for r in range(row-2,-1,-1):
            for c in range(col-1,-1,-1):
                # if r==(row-1):
                #     continue
                if c<len(triangle[r]):
                    dp[r][c]=min(triangle[r][c]+dp[r+1][c],triangle[r][c]+dp[r+1][c+1])
        return dp[0][0]
       

            