class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=0
        for r in t:
            if l==len(s):
                return True
            if r==s[l]:
                l+=1
        return l==len(s) 
        
        
        