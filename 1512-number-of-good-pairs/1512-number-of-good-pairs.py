class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numCount=Counter()
        result=0
        for num in nums:
            if numCount[num]>0:
                result+=numCount[num]
            numCount[num]+=1
        return result
