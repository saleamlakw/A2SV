class Solution(object):
    def removeDuplicates(self, nums):
        n=len(set(nums))
        co=Counter()
        l=1
        for i in range(n):
            co[nums[i]]+=1
            if co[nums[i]]>1:
                while l<len(nums) and co[nums[l]]>=1:
                    l+=1
                if l<len(nums):
                    nums[i],nums[l]=nums[l],nums[i]
                    co[nums[i]]+=1
                    co[nums[l]]-=1
        return n
            
        