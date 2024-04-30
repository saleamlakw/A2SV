class Solution:
    def countBits(self, n: int) -> List[int]:
        re=[]
        for i in range(n+1):
            count=0
            while i:
                count+=(i&1)
                i>>=1
            re.append(count)
        return re
