class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        for i in s:
            if i.isalnum() :
                a.append(i)
        ss="".join(a).lower()
        if ss==ss[::-1]:
            return(True)
        else:
            return(False)
