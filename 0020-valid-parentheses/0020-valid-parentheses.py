class Solution:
    def isValid(self, s: str) -> bool:
        ha={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                 if stack and i in ha:
                     if stack[-1]!=ha[i]:
                         return False
                     stack.pop()
                 else:
                     return False
        return True if not stack else False
        
                
            

        

            