class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*(len(nums)+2)
        for i in range(len(nums)-1,-1,-1):
                take=nums[i]+dp[i+2]
                notake=dp[i+1]
                dp[i]=max(take,notake)
        return dp[0]
        
       