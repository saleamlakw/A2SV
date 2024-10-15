class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo={}
        # def dp(i):
        #     if i>=len(nums):
        #         return 0
        #     if i not in memo:
        #         take = nums[i]+dp(i+2)
        #         nottake = dp(i+1)
        #         memo[i] = max(take,nottake)
        #     return memo[i]
        # return dp(0)
        dp=[float("-inf")]*(len(nums)+2)
        dp[len(nums)]=0
        dp[len(nums)+1]=0
        for i in range(len(nums)-1,-1,-1):
            take = nums[i]+dp[i+2]
            nottake = dp[i+1]
            dp[i] = max(take,nottake)
        return dp[0]

