class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        l=0
        re=0
        
        nums=list(set(nums))
        nums.sort()
        # print(nums)
        for r in range(len(nums)):
            if r>0 and r<len(nums) and nums[r]-nums[r-1]!=1:
                l=r
            re=max(re,r-l+1)
        return re
