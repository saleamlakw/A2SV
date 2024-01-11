class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=1
        while r<len(nums):
            print(nums[r-1],nums[r])
            if nums[l]!=nums[r]:
                nums[l+1],nums[r]=nums[r],nums[l+1]
                l+=1
            r+=1
        return l+1
        