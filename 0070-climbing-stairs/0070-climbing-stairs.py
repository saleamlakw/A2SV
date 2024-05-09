class Solution:
    def climbStairs(self, n: int) -> int:
        memo=Counter()
        def fib(n):
            if n<=0:
                return 1
            re=0
            for i in range(1,3):
                if n-i>=0:
                    if n-i not in memo:
                        memo[n-i]=fib(n-i)
                    re+=memo[n-i]
            return re
        return fib(n)
