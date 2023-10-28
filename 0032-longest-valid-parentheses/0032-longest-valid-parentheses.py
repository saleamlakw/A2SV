class Solution:
    def longestValidParentheses(self, s: str) -> int:
        re=0
        is_ok=[0]*len(s)
        stack=[]
        for i,val in enumerate(s):
            if val=="(":
                stack.append(i)
            elif val==")":
                if stack:
                    is_ok[stack.pop()]=1
                    is_ok[i]=1
                    
        result=0
        for k ,val in enumerate(s):
            if val in "()":
                if is_ok[k]:
                    re+=1
                    result=max(result,re)
                else:
                    re=0
        return result