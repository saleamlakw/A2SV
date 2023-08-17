class Solution:
    from itertools import accumulate
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a=[0]+list(accumulate(nums))[:-1]
        b=(list(accumulate(nums[::-1]))[:-1])[::-1]+[0]
        print(a)
        print(b)
        re=[]
        for i in range(len(a)):
            re.append(abs(a[i]-b[i]))
        return re
            