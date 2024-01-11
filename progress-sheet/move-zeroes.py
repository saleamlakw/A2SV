class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l,r=0,1
        while l<len(nums) and r<len(nums):
            while l<len(nums)  and nums[l]!=0:
                l+=1
                if l>=r:
                    r+=1 
            if l<len(nums) and r<len(nums) and nums[r]!=0 and nums[l]==0 and l<r:
                nums[r],nums[l]=nums[l],nums[r]
            r+=1
        