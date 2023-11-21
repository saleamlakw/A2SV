class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        curSum=0
        result=0
        l=0
        for r in range(len(s)):
            curSum+=abs(ord(s[r])-ord(t[r]))
            while l<len(s) and curSum>maxCost:
                curSum-=abs(ord(s[l])-ord(t[l]))
                l+=1
            result=max(result,r-l+1)
        return result
            
        