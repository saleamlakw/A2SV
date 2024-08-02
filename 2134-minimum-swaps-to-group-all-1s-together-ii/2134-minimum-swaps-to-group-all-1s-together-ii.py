class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        if nums.count(1)==0:
            return 0
        nums=nums+nums
        l=0
        ans=float("inf")
        one_count=0
        n=nums.count(1)//2
        for r in range(len(nums)):
            if nums[r]==1:
                    one_count+=1
            while l<r and  r-l+1>n:
                if nums[l]==1:
                    one_count-=1
                l+=1
            if r-l+1==n:
                ans=min(ans,r-l+1-one_count)
        return ans
  

        