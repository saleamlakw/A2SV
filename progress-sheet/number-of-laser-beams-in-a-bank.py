class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        re=0
        l,r=0,1
        while l< len(bank) and r<len(bank):
            ele1=bank[l].count("1")
            ele2=bank[r].count("1")
            while l<len(bank) and not (ele1:=bank[l].count("1")):
               l+=1
            while r<len(bank) and not (ele2:=bank[r].count("1")):
               r+=1
            if ele1*ele2 and l<r:
               re+=ele1*ele2
            l=r
            r+=1
        return re
                
