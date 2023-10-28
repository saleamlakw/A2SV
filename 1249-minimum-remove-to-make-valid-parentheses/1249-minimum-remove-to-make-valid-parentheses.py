class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        is_ok=[0]*len(s)
        stack=[]
        for i,val in enumerate(s):
            if val=="(":
                stack.append(i)
            elif val==")":
                if stack:
                    is_ok[stack.pop()]=1
                    is_ok[i]=1
        ans=""
        for k ,v in enumerate(s):
            if v in "()":
                if is_ok[k]:
                    ans+=v
            else:
                ans+=v
        return ans
            