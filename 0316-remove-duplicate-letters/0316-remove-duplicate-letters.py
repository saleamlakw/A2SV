class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited=set( )
        print(visited)
        dic={}
        for k in range(len(s)):
            dic[s[k]]=k
        stack=[]
        for i in range(len(s)):
            if (s[i]) not in  visited:
                while stack and stack[-1]>s[i] and dic[stack[-1]]>i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
                print(stack)
        print(stack)
        return "".join(stack)
                