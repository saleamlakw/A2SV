class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int: 
        re=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    re+=1
        return re
        
        
