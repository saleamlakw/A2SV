class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        ind={}
        for i in range(len(nums)):
            ind[nums[i]]=i
        for val,rep in operations:
            ind[rep]=ind[val]
            ind.pop(val)
        result=[0]*len(nums)
        for r in ind:
            result[ind[r]]=r
        return result
        