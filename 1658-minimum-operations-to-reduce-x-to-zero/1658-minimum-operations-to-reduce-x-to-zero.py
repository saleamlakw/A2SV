class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total=0
        target=sum(nums)-x
        l=0
        re=-1
        if sum(nums)==x:
            return len(nums)
        if target <=0:
            return -1
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                if total==target:
                    re=max(re,r-l+1)
                print(re)
                total-=nums[l]
                l+=1
        return -1 if re==-1 else len(nums)-re
        