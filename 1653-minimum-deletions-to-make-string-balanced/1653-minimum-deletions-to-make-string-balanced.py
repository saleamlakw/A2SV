class Solution:
    def minimumDeletions(self, s: str) -> int:
        memo=[[None,None] for _ in range(len(s))]
        def dp(pre,i):
            
            if i>=len(s):
                return 0
            if memo[i][pre]==None:
                le=0
                if pre==1 and s[i]=="a":
                    pass
                else:
                    if s[i]=="a":
                        le=1+dp(0,i+1)
                    else:
                        le=1+dp(1,i+1)
                re=dp(pre,i+1) 
                memo[i][pre]=max(le,re)
            return memo[i][pre]
        return len(s)-dp(0,0)
