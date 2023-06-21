class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=set(nums)
        b=set(list(range(0,max(nums)+1)))
        if list(b.difference(a)):
            return(list(b.difference(a))[0])
        else:
            return(max(nums)+1)
