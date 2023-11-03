class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        valid=[0]*len(s)
        for r in range(len(s)):
            if s[r]=="(":
                stack.append(r)
            else:
                if stack and s[stack[-1]]=="(":
                    valid[stack.pop()]=1
                    valid[r]=1
        result=0
        for val in valid:
            if val==0:
                result+=1
        return result