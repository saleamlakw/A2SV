class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        memo = {}
        def dp(i,sum_):
            if sum_ == target:
                return True
            if sum_>target:
                return False
            if i >= len(nums):
                return False
            if (i,sum_) not in memo:
                memo[(i,sum_)] =  dp(i+1,sum_+nums[i]) or  dp(i+1,sum_)
            return memo[(i,sum_)]
        return dp(0,0)