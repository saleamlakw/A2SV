class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        co=Counter(nums)
        tot=0
        for i in co:
            tot+=math.comb(co[i],2)
        return tot
            