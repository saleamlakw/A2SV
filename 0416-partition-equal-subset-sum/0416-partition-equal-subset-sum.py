class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        memo={}
        def fn(i,target):
            # print(i,target)
            if (i,target)  in memo:
                return memo[(i,target)]
            if target==0:
                return True
            if i==len(nums):
                return False
           
            take=False
            if target>=nums[i]:
                take=fn(i+1,target-nums[i])
            if not take :
                not_take=fn(i+1,target)
            memo[(i,target)]=take or not_take
            return memo[(i,target)]
        return fn(0,sum(nums)//2)
        
        