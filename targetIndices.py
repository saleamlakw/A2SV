class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        re=[]
        nums.sort()
        for r,val in enumerate(nums):
            if val==target:
                re.append(r)
        return re
                


       

