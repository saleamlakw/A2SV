class Solution:
    def addBinary(self, a: str, b: str) -> str:
        car="0"
        l=len(a)-1
        r=len(b)-1
        re=""
        while l>=0 and r>=0:
            if a[l]=="1" and b[r]=="1":
                re+=car
                car="1"
            elif a[l]=="0" and  b[r]=="0":
                re+=car
                car="0"
            else:
                if car=="1":
                    re+="0"
                    car="1"
                else:
                    re+="1"
                    car="0"
            l-=1
            r-=1
        # re=re[::-1]
        print(re)
        print(a[:l+1])
        print(b[:r+1])
        while l>=0:
            if a[l]=="1":
                if car=="0":
                    re+="1"
                else:
                    re+="0"
                    car="1"
            else:
                re+=car
                car="0"
            l-=1
        while r>=0:
            if b[r]=="1":
                if car=="0":
                    re+="1"
                else:
                    re+="0"
                    car="1"
            else:
                re+=car
                car="0"
            r-=1
        if car=="1":
            re+="1"
        return re[::-1]
        
        