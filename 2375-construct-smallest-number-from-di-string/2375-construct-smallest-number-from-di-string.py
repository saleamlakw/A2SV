class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result=""
        if pattern[0]=="I":
            s=1
            mx=1
            result+=str(s)
        else:
            s=0
            for g in pattern:
                if g=="D":
                    s+=1
                else:
                    break
            s=s+1
            mx=s
            result+=str(s)
        for r in range(len(pattern)):
            if pattern[r]=="I":
                s=mx
                if r+1<len(pattern):
                    if pattern[r+1]=='D':
                        l=r+1
                        
                        while l<len(pattern) and pattern[l]=='D':
                            s+=1
                            l+=1
                s+=1
                mx=max(mx,s)
                result+=str(s)
            if pattern[r]=='D':
                s-=1
                mx=max(mx,s)
                result+=str(s)
        return result
                