class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        path = defaultdict(bool)
        dp = [[0]*(len(nums)+2) for _ in range(len(nums)+2)]
       
        for pre in range(len(nums)-1,-2,-1):
            for cur in range(len(nums)-1,-1,-1):
                take = float("-inf")
                if pre == -1 or nums[cur]%nums[pre]  == 0:
                    take = 1 + dp[cur][cur+1]
                nottake = dp[pre][cur+1]
                dp[pre][cur] = max(take,nottake)

                path[(pre,cur)] = take > nottake
           

        ans  = []
        pre , cur = -1,dp[-1].index(max(dp[-1]))
        while cur<len(nums):
            if path[(pre,cur)]:
                ans.append(nums[cur])
                pre , cur = cur, cur + 1
            else:
                cur += 1
        return ans
