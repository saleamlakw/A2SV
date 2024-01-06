class Solution:
    def sortColors(self, nums: List[int]) -> None:
       for i in range(1,len(nums)):
           j=i-1
           while j>=0 and nums[j]>nums[j+1]:
               nums[j],nums[j+1]=nums[j+1],nums[j]
               j-=1   
                    