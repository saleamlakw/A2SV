class Solution:
    def isPalindrome(self,s):
        finalString="" #O(n)
        for i in s:
            if i.isalnum():
                finalString+=i #O(n)
        
        finalString=finalString.lower() #O(n)
        
        if not finalString:
            return True
        else:
            l,r=0,len(finalString)-1    
            while l<r:                 #O(n)
                if finalString[l]!=finalString[r]:
                    return False
                r-=1
                l+=1
            return True  