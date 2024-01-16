class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       
        maxAverage=float("-inf")

        l=0
        tot=0
        for r in range(len(nums)):
            tot+=nums[r]
            while r-l+1>k:
                tot-=nums[l]
                l+=1
            if r-l+1==k:
                maxAverage=max(maxAverage,tot/k)
        return maxAverage
        