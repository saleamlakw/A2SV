class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for i in path.split("/"):
            if i=="":
                pass
            elif i==".":
                pass
            elif i=="..":
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(i)
        return "/"+"/".join(stack)
            
                