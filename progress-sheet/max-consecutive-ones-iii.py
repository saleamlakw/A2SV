class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        re=0
        zero=0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero+=1
            while l<len(nums) and zero>k:
                if nums[l]==0:
                    zero-=1
                l+=1
            re=max(re,r-l+1)
        return re
            