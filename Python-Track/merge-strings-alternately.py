class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        l,r=0,0
        while l<len(word1) and r<len(word2):
                result+=(word1[l]+word2[r])
                l+=1
                r+=1
        result+=(word1[l:]+word2[r:])
        return result
            