class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        mi=float("inf")
        ma=float('-inf')
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                mi=min(mi,mid)
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                ma=max(ma,mid)
                l=mid+1
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return [mi,ma] if ma != float('-inf') and mi!=float("inf") else [-1,-1]
            