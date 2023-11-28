class Solution(object):
    def makeSmallestPalindrome(self, s):
        l,r=0,len(s)-1
        re=list(s)
        while l<r:
            if re[l]!=re[r]:
                if re[l]>re[r]:
                    re[l]=re[r]
                else:
                    re[r]=re[l]
            l+=1
            r-=1
        return "".join(re)
                
                
        