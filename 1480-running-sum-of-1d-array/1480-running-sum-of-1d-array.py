class Solution(object):
    def runningSum(self, nums):
        accumulator=0
        prefixSum=[]
        for num in nums:
            accumulator+=num
            prefixSum.append(accumulator)
        return prefixSum