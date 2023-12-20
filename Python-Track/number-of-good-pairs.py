class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        co=Counter(nums)
        re=0
        for r in nums:
            re+=(co[r]-1)
            co[r]=(co[r]-1)
        return re