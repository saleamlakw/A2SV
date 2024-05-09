class Solution:
    def fib(self, n: int) -> int:
            memo=Counter()
            if n<=1:
                return n
            if n not in memo:
                memo[n]=self.fib(n - 1) + self.fib(n - 2)
            return memo[n]
