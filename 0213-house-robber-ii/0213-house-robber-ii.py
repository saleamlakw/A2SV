class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[[0,0] for _ in range(len(nums)+2)]

        for i in range(len(nums)-1,-1,-1):
            for taken in range(2):
                if i==0:
                    take=nums[i]+dp[i+2][1]
                    nottake=dp[i+1][0]
                    dp[i][taken]=max(take,nottake)
                elif i==len(nums)-1:
                    take=float("-inf")
                    if not taken:
                        take=nums[i]+dp[i+2][1]
                    nottake=dp[i+1][0]
                    dp[i][taken]=max(take,nottake)
                else:
                    take=nums[i]+dp[i+2][taken]
                    nottake=dp[i+1][taken]
                    dp[i][taken]=max(take,nottake)
        # memo={}
        # def dp(i,taken):
        #     if i>=len(nums):
        #         return 0
        #     if (i,taken) not in memo:
        #         if i==0:
        #             take=nums[i]+dp(i+2,1)
        #             nottake=dp(i+1,0)
        #             memo[(i,taken)]=max(take,nottake)
        #         elif i==len(nums)-1:
        #             take=float("-inf")
        #             if not taken:
        #                 take=nums[i]+dp(i+2,1)
        #             nottake=dp(i+1,0)
        #             memo[(i,taken)]=max(take,nottake)
        #         else:
        #             take=nums[i]+dp(i+2,taken)
        #             nottake=dp(i+1,taken)
        #             memo[(i,taken)]=max(take,nottake)
        #     return memo[(i,taken)]
        return dp[0][0]

            