class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counterDict=Counter(nums)
        return [i for i in counterDict if counterDict[i]>len(nums)/3]
            