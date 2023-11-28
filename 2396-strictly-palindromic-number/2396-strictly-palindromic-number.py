class Solution(object):
    def isStrictlyPalindromic(self, n):
        def helper(s):
            l,r=0,len(s)-1
            while l<r:
                if s[l] !=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def intTObase(n,base):
            if n==0:
                return "0"
            re=""
            while n:
                re+=str(n%base)
                n=n//base
            print(re)
            return re[::-1]
        for base in range(2,n-1):
            if not helper(intTObase(n,base)):
                return False
        return True
            
            
           
        