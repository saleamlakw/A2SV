class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def numberOfSteps(x):
            if x == 1:
                return 0
            if x not in memo:
                ans = 0
                if x%2 == 0:
                    ans += (1+ numberOfSteps(x//2))
                else:
                    ans +=(1 + numberOfSteps(3 * x + 1))
                memo[x] = ans
            return memo[x]
        numbers = []
        for num in range(lo,hi+1):
            numbers.append([num,numberOfSteps(num)])
        
        numbers.sort(key = lambda x : (x[1],x[0]))
        return numbers[k-1][0]