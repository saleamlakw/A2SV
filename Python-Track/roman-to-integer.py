class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}
        r=0
        re=0
        while r<len(s):
            if s[r]=="I":
                if r+1<len(s) and s[r+1]=="V":
                    re+=4
                    r+=1
                elif r+1<len(s) and s[r+1]=="X":
                    re+=9
                    r+=1
                else:
                    re+=1
            elif s[r]=="X":
                if r+1<len(s) and s[r+1]=="L":
                    re+=40
                    r+=1
                elif r+1<len(s) and s[r+1]=="C":
                    re+=90
                    r+=1
                else:
                    re+=10
            elif s[r]=="C":
                if r+1<len(s) and s[r+1]=="D":
                    re+=400
                    r+=1
                elif r+1<len(s) and s[r+1]=="M":
                    re+=900
                    r+=1
                else:
                    re+=100
            else:
                re+=hashmap[s[r]]
            r+=1
        return re
    
    
