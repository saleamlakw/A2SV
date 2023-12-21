class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        w2=""
        for r in word1:
            w1+=r
        for l in word2:
            w2+=l
        return w1==w2