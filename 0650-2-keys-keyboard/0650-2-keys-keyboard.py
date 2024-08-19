class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        memo={}
        def dp(op,w,v):
            print(op,w,v)
            if w==n:
                return 0
            if w>n:
                return float("inf")
            if (op,w,v) not in memo:
                paste=1+dp(1,w+v,v)
                copy=2+dp(0,w+w,w)
                memo[(op,w,v)]=min(copy,paste)
            return memo[(op,w,v)]
        return 2+dp(1,2,1)

