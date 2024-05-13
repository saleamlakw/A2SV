class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo=Counter() #--->o(n)+2*o(n)
        def inbound(r,c):
            return 0<=r<m and 0<=c<n
        def dp(r,c):
            if r==0 and c==0:
                return 1
            if not inbound(r,c):
                return 0
            if (r,c) not in memo: 
                memo[(r,c)]= dp(r-1,c)+dp(r,c-1)
            return memo[(r,c)]
        return dp(m-1,n-1)
            