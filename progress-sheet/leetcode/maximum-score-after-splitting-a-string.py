class Solution:
    def maxScore(self, s: str) -> int:
        one=s.count("1")
        zero=0
        result=0
        for ele in s[:-1]:
            if ele=="0":
                zero+=1
            else:
                one-=1
            result=max(result,one+zero)
        return result