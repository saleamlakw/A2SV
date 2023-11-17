class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalnum() :
                a+=i
        aa=a.lower()
        return aa==aa[::-1]