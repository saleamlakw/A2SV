class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        t=ceil(log2(len(nums)))+1
        # print(t)
        ans=float("inf")
        for _ in range(t):
            m=(l+r)//2
            # print(m,nums[m])
            ans=min(ans,nums[m])
            if nums[0]<=nums[m]<=nums[-1]:
                return nums[0]
            elif nums[m]>=nums[0]:
                l=m+1
            else:
                r=m-1
        return ans
