class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo=Counter()
        def fn(i,target):
            if i>=len(nums):
                if target==0:
                    return 1
                else:
                    return 0
            if (i,target) not in memo:
                l=fn(i+1,target-nums[i])
                r=fn(i+1,target+nums[i])
                memo[(i,target)]=l+r
            return memo[(i,target)]
        return fn(0,target)
