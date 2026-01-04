class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(n):
            ans = set()

            for i in range(1,int(n**0.5)+1):
                if n%i == 0:
                    ans.add(i)
                    d = n//i
                    if n%d == 0:
                        ans.add(d)
            if len(ans) == 4:
                return sum(ans)
            return 0
        ans = 0
        for num in nums:
            ans += divisors(num)
        return ans
