class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r=0
        while l<=r and r<len(nums):
            if nums[r]==val:
                r+=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r+=1
        return l