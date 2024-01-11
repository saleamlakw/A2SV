class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        s.sort(key=lambda x:int(x[-1]))
        for i in range(len(s)):
            s[i]=s[i][:-1]
        return " ".join(s)
