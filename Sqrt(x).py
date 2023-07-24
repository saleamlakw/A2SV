class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        res=0
        while l<=r:
            mid=(l+r)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                res=max(mid,res)
                l=mid+1
            else:
                r=mid-1
        return res
