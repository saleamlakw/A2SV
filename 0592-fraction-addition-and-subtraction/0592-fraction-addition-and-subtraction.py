class Solution:
    def fractionAddition(self, expression: str) -> str:
        from fractions import Fraction
        pre=""
        sign=""
        r=0
        while r<len(expression):
            fra=""
            
            while r<len(expression):
                if expression[r] in "-+" and r-1>0:
                    break
                fra+=expression[r] 
                r+=1
            if pre!="":
                if sign=="+":
                    pre+=(Fraction(fra))
                else:
                    pre-=(Fraction(fra))
            else:
                pre=Fraction(fra)
            sign=expression[r] if r<len(expression) else ""
            r+=1
            
            fra=""
        if int(pre)==pre:
            return str(pre)+"/"+"1"
        return str(pre)
                    


