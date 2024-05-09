class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=n)
        def fib(n):
            if n<=0:
                return 1
            re=0
            for i in range(1,3):
                if n-i>=0:
                    re+=fib(n-i)
            return re
        return fib(n)
