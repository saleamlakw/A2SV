class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls=[]
        for ele in s:
            if ele.isalnum():
                ls.append(ele.lower())
        l,r=0,len(ls)-1
        while l<r:
            if ls[l]!=ls[r]:
                return False
            l+=1
            r-=1
        return True

