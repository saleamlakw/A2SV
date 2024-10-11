class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
            before=[]
            stack=[]
            i=0
            def check(stack,ele):
                if stack and stack[-1][0]==ele:
                    return stack[-1][1]>=(k-1)
                return False
                
            for i in range(len(s)):
                if check(stack,s[i]):
                    for _ in range(k-1):
                        if stack :
                            stack.pop()
                        else:
                            break
                else:
                    if stack and stack[-1][0]==s[i]:
                        stack.append([s[i],stack[-1][1]+1])
                    else:
                        stack.append([s[i],1])
            ans=[]
            for char,count in stack:
                ans.append(char)

            return "".join(ans)
                



            