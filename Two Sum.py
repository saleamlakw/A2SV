class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        re={}
        for i,value in enumerate(nums):
            if target-value in re:
                return [i,re[target-value]]
            else:
                re[value]=i
