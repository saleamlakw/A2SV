class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        col=len(original)/m
        if col!=n:
            return []
        else:
            ans=[]
            re=[]
            k=0
            for i in range(len(original)):
                re.append(original[i])
                k+=1
                if k==n:
                    ans.append(re)
                    re=[]
                    k=0
            return ans

