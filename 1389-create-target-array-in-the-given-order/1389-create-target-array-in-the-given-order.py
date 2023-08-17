class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        re=[]
        for i in range(len(nums)):
            re.insert(index[i],nums[i])
        return re
        