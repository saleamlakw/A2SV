class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        re=[]
        all=sorted(nums)
        for i in nums:
            re.append(len(all[:all.index(i)]))
        return re
