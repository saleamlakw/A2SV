class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        cursum=0
        for i in nums:
            cursum=max(0,cursum)
            cursum+=i
            maxsum=max(maxsum,cursum)
        return maxsum