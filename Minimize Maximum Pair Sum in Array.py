class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ma=0
        l=0
        r=len(nums)-1
        while l<r:
            ma=max(ma,nums[l]+nums[r])
            l+=1
            r-=1
        return ma


        
