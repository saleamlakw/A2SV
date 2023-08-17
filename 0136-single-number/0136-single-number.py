class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        all=Counter(nums)
        for i in all:
            if all[i]==1:
                return i
        