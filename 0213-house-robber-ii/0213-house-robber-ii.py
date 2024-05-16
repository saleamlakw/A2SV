class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def dp(i,taken):
            if i>=len(nums):
                return 0
            if (i,taken) not in memo:
                if i==0:
                    take=nums[i]+dp(i+2,1)
                    nottake=dp(i+1,0)
                    memo[(i,taken)]=max(take,nottake)
                elif i==len(nums)-1:
                    take=float("-inf")
                    if not taken:
                        take=nums[i]+dp(i+2,1)
                    nottake=dp(i+1,0)
                    memo[(i,taken)]=max(take,nottake)
                else:
                    take=nums[i]+dp(i+2,taken)
                    nottake=dp(i+1,taken)
                    memo[(i,taken)]=max(take,nottake)
            return memo[(i,taken)]
        return dp(0,0)

            