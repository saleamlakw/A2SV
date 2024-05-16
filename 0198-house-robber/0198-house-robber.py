class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[-1]*len(nums)
        def dp(i):
            if i>=len(nums):
                return 0
            if memo[i]==-1:
                take=nums[i]+dp(i+2)
                notake=dp(i+1)
                memo[i]=(max(take,notake))
            return memo[i]
        return dp(0)
       