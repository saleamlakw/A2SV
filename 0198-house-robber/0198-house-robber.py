class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0 
            if i not in memo:
                take = nums[i] + dp(i+2)
                nottake = dp(i+1)
                memo[i] = max(take , nottake)
            return memo[i]
        return dp(0)
            

