class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accumulator=0
        for i in range(len(nums)):
            accumulator+=nums[i]
            nums[i]= accumulator
        return nums
