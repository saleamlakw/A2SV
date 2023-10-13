class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp, dp1, dp2 = 0, 0, 0
        for i in range(2, n + 1):
            oneStep = dp1 + cost[i - 1]
            twoStep = dp2 + cost[i - 2]
            dp = min(oneStep, twoStep)
            dp2 = dp1
            dp1 = dp
        return dp1
        