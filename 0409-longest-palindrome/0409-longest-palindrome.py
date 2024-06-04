class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss=Counter(s)
        odd=0
        re=len(s)
        for i in ss:
            if ss[i]%2!=0 and odd>=1:
                re-=1
            if ss[i]%2!=0:
                odd+=1
        return re
