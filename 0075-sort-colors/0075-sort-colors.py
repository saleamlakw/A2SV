class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1,len(nums)):
            j=i-1
            while nums[j+1]<nums[j] and j >=0:
                nums[j+1],nums[j]=nums[j],nums[j+1]
                j-=1
        return nums
        