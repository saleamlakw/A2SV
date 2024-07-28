class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    
        tot=sum(nums)
        n=len(nums)
        if tot%k!=0:
            return False 
        
        target=tot//k
        memo={}
        def backtrack(re,mask):
            if mask==(1<<n)-1:
                return True
            if re==target:
                return backtrack(0,mask)
            if (re,mask) not in memo:
                temp=False
                for j in range(n):
                    if mask&(1<<j) or  re+nums[j]>target:
                        continue
                    temp=temp or backtrack(re+nums[j],mask|(1<<j))
                memo[(re,mask)]=temp
            return memo[(re,mask)]
        return backtrack(0,0)
