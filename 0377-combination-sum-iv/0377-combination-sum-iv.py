class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo=[-1]*(target+1)
        def dp(target):
            if target==0:
                return 1
            if target < 0:
                return 0
            if memo[target]==-1:
                re=0
                for i in nums:
                    re+=dp(target-i)
                memo[target]=re
            return memo[target]
        return dp(target)