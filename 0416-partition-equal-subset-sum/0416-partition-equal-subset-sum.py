class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        # dp=[0]*len()
        memo={}
        def dp(target,i):
            if target==0:
                return True
            if target<0:
                return False
            if i>=len(nums):
                return False
            if (target,i) not in memo:
                memo[(target,i)]=dp(target-nums[i],i+1) or dp(target,i+1)
            return memo[(target,i)]
        return dp(target,0)

            
