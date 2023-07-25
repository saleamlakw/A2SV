class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[]
        l,r=0,len(nums)-1
        re=100000000
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                re=min(re,mid)
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        if re==100000000:
            result.append(-1)
        else:
            result.append(re)
        re2=-1
        l2,r2=0,len(nums)-1
        while l2<=r2:
            mid2=(l2+r2)//2
            if nums[mid2]==target:
                re2=max(re2,mid2)
                l2=mid2+1
            elif nums[mid2]>target:
                r2=mid2-1
            else:
                l2=mid2+1
        result.append(re2)
        return result
