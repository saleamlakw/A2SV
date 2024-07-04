class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res=0
        if k:
            res+=(1*min(numOnes,k))
            k-=min(numOnes,k)
        if k:
            k-=min(numZeros,k)
        if k:
            res-=(1*k)
        return res
        
