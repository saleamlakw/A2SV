class Solution:
    from math import ceil
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        while left<right:
            mid=(left+right)//2
            total=sum(ceil(num/mid) for num in nums)
            if total>threshold:
                left=mid+1
            else:
                right=mid
        return left
            