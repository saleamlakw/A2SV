class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        aset = set()
        bset = set()
        all = set()
        ans=[]
        for i in range(len(A)):
            aset.add(A[i])
            bset.add(B[i])
            if A[i] in bset:
                all.add(A[i])
            if B[i]  in aset:
                all.add(B[i])
            ans.append(len(all))
        return ans
            
