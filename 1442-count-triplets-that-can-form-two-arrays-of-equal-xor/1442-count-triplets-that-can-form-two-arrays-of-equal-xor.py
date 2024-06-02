class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        psXor=[0]
        result=0
        for num in arr:
            psXor.append(psXor[-1]^num)
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if psXor[j+1]^psXor[i]==0:
                   result+=(j-i)
        return result