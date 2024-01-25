class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ps1=[]
        accumulator=0
        for num in nums:
            accumulator+=num
            ps1.append(accumulator)
        
        ps2=[]
        acc=0
        for ele in nums[::-1]:
            acc+=ele
            ps2.append(acc)
        ps2.reverse()
        # print(ps1)
        # print(ps2)
        for i in range(len(ps1)):
            if ps1[i]==ps2[i]:
                return i
        return -1


