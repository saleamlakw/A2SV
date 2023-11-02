class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=[]
        stack=[]
        for r in  range(len(s)):
            if s[r]==")":
                if stack and s[stack[-1]]=="(":
                    poped= stack.pop()
                if r-poped==1:
                    score[-1]=(poped,1)
                else:
                    re=0
                    while score[-1]!=poped:
                        re+=score.pop()[1]
                    score.pop()
                    score.append((poped,2*re))
            else:
                stack.append(r)
                score.append(r)
        result=0
        for k in score:
            result+=k[1]
        return result