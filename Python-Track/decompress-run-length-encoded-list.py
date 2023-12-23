class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(0,len(nums),2):
            for k in range(nums[i]):
                result.append(nums[i+1])
        return result

        