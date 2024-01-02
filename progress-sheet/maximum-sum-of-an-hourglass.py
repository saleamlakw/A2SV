class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        r=0
        result=0
        while r+2<len(grid):
            c=0
            while c+2<len(grid[0]):
                re=0
                re+=sum(grid[r][c:c+3])
                re+=grid[r+1][c+1]
                re+=sum(grid[r+2][c:c+3])
                c+=1
                result=max(result,re)
            r+=1
        return result