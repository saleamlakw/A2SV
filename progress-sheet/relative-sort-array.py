class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cc=Counter(arr1)
        result=[]
        for i in arr2:
            for j in range(cc[i]):
                result.append(i)
            cc[i]=0
        
        re1=[]
        for j in cc:
            if cc[j]!=0:
                for h in range(cc[j]):
                    re1.append(j)
        re1.sort()
        return result+re1

        
        return result


        