class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ss=list(s)
        ss.sort(reverse=True,key=lambda x:int(x))
        return "".join(ss[1:]+[ss[0]])