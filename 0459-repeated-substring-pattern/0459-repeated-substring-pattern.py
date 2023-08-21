class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def check(i,s):
            ch=s[:i]
            for k in range(0,len(s),i):
                if ch!=s[k:k+i]:
                    return False
            return True
        if len(s)==1:
            return False
        for j in range((len(s)//2)):
            if check(j+1,s):
                return(True)
        return(False)
            
                
        