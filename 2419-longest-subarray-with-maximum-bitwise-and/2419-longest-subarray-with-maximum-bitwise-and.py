class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        k=max(nums)
        ans=0
        for r in range(len(nums)):
            if nums[r]!=k:
                l=r+1
            if l<len(nums) and r<len(nums) and nums[l]==k and nums[r]==k:
                ans=max(r-l+1,ans)
        return ans
