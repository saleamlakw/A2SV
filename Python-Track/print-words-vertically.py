class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split()
        la=len(max(s,key=lambda x:len(x)))
        re=[""]*la
       
        for r in s:
            for l in range(len(r)):
                re[l]+=r[l]
            for k in range(len(r),la):
                re[k]+=" "
        for t in range(len(re)):
            ne=""
            h=len(re[t])-1
            while h>=0:
                if re[t][h]==" ":
                    h-=1
                else:
                    break
            re[t]=re[t][:h+1]
        return (re)
        