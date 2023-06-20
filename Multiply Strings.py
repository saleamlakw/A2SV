class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        rem=0
        tot=0
        ree=""
        for i in reversed(range(len(num1))):
            rem=0
            ree=""
            for j in reversed(range(len(num2))):
                re=int(num1[i])*int(num2[j])+rem
                if j==0:
                    ree=str(re)+ree[::-1]
                    break
                if re>9:
                    ree+=str(re)[-1]
                    rem=int(str(re)[0])
                else:
                    ree+=str(re)
                    rem=0
            rer=("0"*((len(num1)-1)-i))
            tot+=int(ree+rer)
        return str(tot)

