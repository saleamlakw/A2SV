class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        mi=float('inf')
        ma=float('-inf')
        for i in range(len(nums)):
            if nums[i]==target:
                mi=min(mi,i)
                ma=max(ma,i)
        return [mi,ma] if mi!=float('inf') and ma!=float('inf') else [-1,-1]