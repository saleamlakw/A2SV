class Solution:
    from math import ceil
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        while l<r:
            mid=(l+r)//2
            tot=sum(ceil(i/mid) for i in nums)
            if tot>threshold:
                l=mid+1
            else:
                r=mid
        return l
            