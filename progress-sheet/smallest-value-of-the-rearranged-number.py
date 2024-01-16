class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        elif num>0:
            zero=0
            re=[]
            for i in str(num):
                
                if i=="0":
                    zero+=1
                else:
                    re.append(int(i))
            
            re.sort()
            result=[str(re[0])]
            
            for _ in range(zero):
                result.append("0")

            for e in range(1,len(re)):
                result.append(str(re[e]))
            print(result)
            return int("".join(result))
        else:
            re=[]
            for j in str(num):
                if j!="-":
                    re.append(j)
            print(re)
            re.sort(key=lambda x: int(x),reverse=True)
            re=["-"]+re
            return int("".join(re))

        