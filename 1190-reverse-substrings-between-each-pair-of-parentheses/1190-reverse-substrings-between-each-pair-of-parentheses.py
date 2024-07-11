class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        sa=list(s)
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            if s[i]==")":
                sa[stack[-1]:i+1]=(["0"]+sa[stack[-1]+1:i][::-1]+["0"])
                stack.pop()
        re="".join("".join(sa).split("0"))
        return re

     