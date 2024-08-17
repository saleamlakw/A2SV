class Solution:
    def integerBreak(self, n: int) -> int:
        memo={}
        
        def dp(target):
            if target==0:
                return 1
            if target<0:
                return float("-inf")
            if target not in memo:
                re=float("-inf")
                for i in range(1,n):
                    re=max(re,i*dp(target-i))
                memo[target]=re
            return memo[target]
        return dp(n)
