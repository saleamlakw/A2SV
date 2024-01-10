class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cc={}
        sorted_num=list(sorted(nums))
        for i in range(len(sorted_num)):
            if sorted_num[i] not in cc:
                 cc[sorted_num[i]]=i
        return [cc[k] for k in nums]