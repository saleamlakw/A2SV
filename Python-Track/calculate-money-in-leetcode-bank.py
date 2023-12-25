class Solution:
    def totalMoney(self, n: int) -> int:
        i=1
        re=0
        while (n>7):
            for r in range(i,i+7):
                re+=r
            n-=7
            i+=1
        for j in range(i,n+i):
            re+=j
        return re

