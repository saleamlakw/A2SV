class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing=1
        patch=0
        index=0

        while missing<=n:
            if index<len(nums) and nums[index]<=missing:
                missing+=nums[index]
                index+=1
            else:
                patch+=1
                missing+=missing
            
        return patch
       
          

                       