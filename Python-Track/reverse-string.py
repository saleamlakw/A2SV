class Solution:
    def Reverse(self,s,l,r):
        if l>r:
            return 
        s[l],s[r]=s[r],s[l]
        self.Reverse(s,l+1,r-1)
        return s
    def reverseString(self, s: List[str]) -> None:
        l=0
        r=len(s)-1
        return self.Reverse(s,l,r)
        