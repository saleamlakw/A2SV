class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        def helper(indx, curr_max, cost, m, dp):

            tpl = (indx, curr_max, cost)

            if tpl in dp:
                return dp[tpl]

            if indx == 1 and cost == 1:
                return 1
            elif indx == 1 or cost == 0:
                return 0
            
            numberWays = 0

            for j in range(1, m+1):
                if j <= curr_max:
                    numberWays += helper(indx-1, curr_max, cost, m, dp)
                else:
                    numberWays += helper(indx-1, j, cost-1, m, dp)
            dp[tpl] = numberWays % MOD

            return dp[tpl]

        ans = 0

        dp = {}

        for j in range(1, m+1):
            ans = (ans + helper(n, j, k, m, dp)) % MOD
            
        return ans
                    
                
        