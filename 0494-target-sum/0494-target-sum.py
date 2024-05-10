class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo=Counter()
        def fn(i,target):
            if (i,target) in memo:
                return memo[(i,target)]
            if i>=len(nums):
                if target==0:
                    return 1
                else:
                    return 0
            if (i,target) not in memo:
                memo[(i,target)]=fn(i+1,target-nums[i])+fn(i+1,target+nums[i])
            return memo[(i,target)]
        return fn(0,target)
