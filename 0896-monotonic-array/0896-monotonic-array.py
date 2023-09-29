class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mono_dec=True
        mono_inc=True
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                mono_inc=False
            if nums[i-1]<nums[i]:
                mono_dec=False
            if mono_dec==False and mono_inc==False:
                return False
        return True
            