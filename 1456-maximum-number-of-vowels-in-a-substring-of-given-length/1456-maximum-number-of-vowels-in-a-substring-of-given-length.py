class Solution(object):
    def maxVowels(self, s, k):
        result=0
        vowel=0
        l=r=0
        while r<len(s) and l<len(s):
            if s[r] in "aeiou":
                vowel+=1
            while l<len(s) and r-l+1>k:
                if s[l] in "aeiou":
                    vowel-=1
                l+=1
            if (r-l+1)==k:
                result=max(result,vowel)
            r+=1
        return result