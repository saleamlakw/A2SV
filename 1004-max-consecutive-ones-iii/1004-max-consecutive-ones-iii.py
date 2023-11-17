class Solution(object):
    def longestOnes(self, nums, k):
        co=Counter()
        re=0
        l=0
        for r,num in enumerate(nums):
            if num ==0:
                co[num]+=1
            # print(co)
            while co[0]>k and l<len(nums):
                if l<len(nums) and nums[l]==0:
                    co[0]-=1
                l+=1
            if co[0]<=k:
                re=max(re,r-l+1)
        return re
        