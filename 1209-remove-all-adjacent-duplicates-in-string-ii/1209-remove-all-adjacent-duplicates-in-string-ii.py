class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
            before=[]
            stack=[]
            i=0
            def check(stack,ele):
                count=1
                j=len(stack)-1
                while j>=0 and stack and stack[j]==ele:
                    j-=1
                    count+=1
                return count>=(k)
                
            for i in range(len(s)):
                if check(stack,s[i]):
                    for _ in range(k-1):
                        if stack :
                            stack.pop()
                else:
                    stack.append(s[i])
            return "".join(stack)
                



            