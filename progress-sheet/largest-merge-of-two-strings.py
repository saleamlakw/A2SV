class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l,r=0,0
        result=[]
        while word1 and word2:
            if word1>word2:
                result.append(word1[0])
                word1=word1[1:]
            else:
                result.append(word2[0])
                word2=word2[1:]
        
        if word1:result+=list(word1)
        
        if word2:result+=list(word2)
        return "".join(result)

