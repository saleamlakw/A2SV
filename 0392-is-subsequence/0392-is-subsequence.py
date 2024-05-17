class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        memo=[[-1]*m for _ in range(n)]
        def dp(i,j):
            if i>=n:
                return True
            if j>=m:
                return False
            if memo[i][j]==-1:
                if s[i]==t[j]:
                    memo[i][j]=dp(i+1,j+1)
                else:
                    memo[i][j]=dp(i,j+1)
            return memo[i][j]
        return dp(0,0)