class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row=len(triangle)
        memo={}
        def dp(r,c):
            if r>=row:
                return float("inf")
            if r==(row-1):
                return triangle[r][c]
            if (r,c) not in memo:
                if r+1<row:
                    re=float("inf")
                    for j in range(len(triangle[r+1])):
                        re=min(re,triangle[r][c]+dp(r+1,j))
                    memo[(r,c)]=re
            return memo[(r,c)]
        return dp(0,0)

            