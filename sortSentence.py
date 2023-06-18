class Solution:
    def sortSentence(self, s: str) -> str:
        dic={}
        all=s.split()
        re=[]
        for i in all:
            dic[int(i[-1])]=i[:-1]
        for k in range(1,len(all)+1):
            re.append(dic[k])
        return " ".join(re)
