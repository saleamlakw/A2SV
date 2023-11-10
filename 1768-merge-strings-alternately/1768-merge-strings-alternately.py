class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        l,r=0,0
        switch=True
        while l<len(word1) and r<len(word2):
                result+=word1[l]
                l+=1
                result+=word2[r]
                r+=1
        if l<len(word1):
            result+=word1[l:]
        if r<len(word2):
            result+=word2[r:]
        return result
                
            