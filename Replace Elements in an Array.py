class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        a={}
        for i,v in enumerate(nums):
            a[v]=i
        for k in operations:
            nums[a[k[0]]]=k[1]
            a[k[1]]=a[k[0]]
        return nums
            
