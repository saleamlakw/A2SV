class Solution:
    def maxProduct(self, words: List[str]) -> int:
        result=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(set(words[i]).intersection(set(words[j])))==0:
                    result=max(result,len(words[i])*len(words[j]))
        return result

