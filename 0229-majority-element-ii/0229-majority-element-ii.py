class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counterDict=Counter(nums)
        re=[]
        for i in counterDict:
            if counterDict[i]>len(nums)/3:
                re.append(i)
        return re
            