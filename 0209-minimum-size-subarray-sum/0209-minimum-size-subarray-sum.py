class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total=0
        l=0
        re=float('inf')
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                re=min(re,r-l+1)
                total-=nums[l]
                l+=1
        return 0 if re==float('inf') else re