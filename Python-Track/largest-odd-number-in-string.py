class Solution:
    def largestOddNumber(self, num: str) -> str:
        re=""
        s=""
        for r in num:
            s+=r
            if int(r)%2!=0:
                re=s
        return re