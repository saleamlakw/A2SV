class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        memo = {}
        
        def helper(total, i):
            nonlocal nums, memo
            if (total, i) in memo:
                return memo[(total, i)]
            if i == len(nums):
                return False
            if total == 0:
                return True
            memo[(total, i)] = helper(total-nums[i], i+1) or helper(total, i+1)
            return memo[(total, i)]
        
        return helper(target, 0) 