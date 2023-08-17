class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        all=Counter(nums)
        ma=float('-inf')
        va=0
        for i in all:
            if all[i]>ma:
                ma=all[i]
                va=i
        return va
                