class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq=[0]*len(nums)
        for l,r in requests:
            freq[l]+=1
            if r+1<len(nums):
                freq[r+1]-=1
        freq=list(accumulate(freq))
        freq.sort()
        nums.sort()
        re=0
        for i in range(len(nums)):
            re+=(nums[i]*freq[i])
        return (re)%(10**9+7)

            