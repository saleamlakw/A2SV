class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0 , len(nums)-1
        ans = float("inf")

        while r >= l:
            m = (l+r)//2
            ans = min(ans,nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r= m - 1
        return ans