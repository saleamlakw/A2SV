class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot=sum(nums)
        n=len(nums)
        if tot%k!=0:
            return False
        
        h=tot//k
        def backtrack(i,re):
            # print(i,re)
            if re==h:
                return True
            if i>=n or re>h:
                return False
            re1=False
            if nums[i]:
                re1=backtrack(i+1,re+nums[i]) 
            if re1:
                nums[i]=None
                return re1
            re2=backtrack(i+1,re)
            return re1 or re2
        while k:
            res=backtrack(0,0)
            # print(res)
            # print(nums)
            if not res:
                return False
            k-=1
        return True