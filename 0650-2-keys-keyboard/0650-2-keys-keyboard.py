class Solution:
    def minSteps(self, n: int) -> int:
        
        if n==1:
            return 0
        dp=[[float("inf")]*(n+1) for _ in range(n)]
        dp+=[[0]*(n+1)]
        # print(dp)
        for w in range(n,-1,-1):
            for v in range(n,-1,-1):
                if w==n:
                    continue
                if dp[w][v]==float("inf"):
                    paste=dp[w+v][v] if w+v<=n else float("inf")
                    copy=dp[w+w][w] if w+w<=n else float("inf")
                    dp[w][v]=min(2+copy,1+paste)
        return 2+dp[2][1]
