class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        all=[]

        for i in range(len(arrays)):
            all.append([arrays[i][0],i])
            all.append([arrays[i][-1],i])
        all.sort()
        res=0

        print(all)
        l,r=0,len(arrays)

        if all[0][1]!=all[-1][1]:
            res=max(res,abs(all[0][0]-all[-1][0]))
        if all[0][1]!=all[-2][1]:
            res=max(res,abs(all[0][0]-all[-2][0]))
        if all[1][1]!=all[-1][1]:
            res=max(res,abs(all[1][0]-all[-1][0]))
        
        return res