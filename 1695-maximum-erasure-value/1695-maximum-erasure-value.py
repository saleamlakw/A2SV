class Solution(object):
    def maximumUniqueSubarray(self, nums):
        result=0
        unique=0
        total=0
        co=Counter() #----n
        l=0
        for r in range(len(nums)): #---- n
            total+=nums[r]
            co[nums[r]]+=1
            if co[nums[r]]==1:
                unique+=1
            while l<len(nums) and (r-l+1)>unique:
                total-=nums[l]
                co[nums[l]]-=1
                if co[nums[l]]==0:
                    unique-=1
                l+=1
            if (r-l+1)==unique:
                result=max(result,total)
        return result 