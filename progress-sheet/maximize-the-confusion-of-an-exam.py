class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t=0
        f=0
        res=0
        l=0
        for r in range(len(answerKey)):
            if answerKey[r]=="T":
                t+=1
            else:
                f+=1
            while l<len(answerKey) and min(t,f)>k:
                if answerKey[l]=="T":
                    t-=1
                else:
                    f-=1
                l+=1
            res=max(res,r-l+1)
        return res