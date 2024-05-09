class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=len(nums))
        def fn(n):
            if n==(len(nums)-1):
                return nums[n]
            if n>=(len(nums)):
                return 0
            re=float("-inf")
            for i in range(2,4):
                re=max(re,fn(n+i))
            print(re,n)
            return re+nums[n]
        return max(fn(0),fn(1)) if len(nums)>1 else fn(0)
       