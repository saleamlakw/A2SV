class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n=len(dungeon)
        m=len(dungeon[0])
        def inbound(r,c):
            return 0<=r<n and 0<=c<m
        memo={}
        def dp(i,j):
            if not inbound(i,j):
                return float("-inf")
            if i==n-1 and j==m-1:
                return dungeon[i][j]
            if (i,j) not in memo:
                down=min(dp(i+1,j)+dungeon[i][j],dungeon[i][j])
                right=min(dp(i,j+1)+dungeon[i][j],dungeon[i][j])
                memo[(i,j)]= max(down,right)
            return memo[(i,j)]
        return (max(0,-1*dp(0,0))+1)
           
            