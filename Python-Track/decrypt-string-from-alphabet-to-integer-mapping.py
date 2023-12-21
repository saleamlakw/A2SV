class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashmap=dict(zip(list(range(1,27)),list("abcdefghijklmnopqrstuvwxyz")))
        stack=[]
        res=""
        r=0
        while r<len(s):
            # print(stack)
            if len(stack)==2 and s[r]!="#":
                if r+1<len(s) and s[r+1]=="#":
                    res+=hashmap[int(stack[0])]
                    res+=hashmap[int(stack[-1]+s[r])]
                    stack.pop()
                    stack.pop()
                    r+=1
                else:
                    res+=hashmap[int(stack[0])]
                    res+=hashmap[int(stack[1])]
                    stack.pop()
                    stack.pop()
            elif len(stack)==2 and s[r]=="#":
                
                res+=hashmap[int("".join(stack))]
                stack.pop()
                stack.pop()
            if s[r]!= "#":
                stack.append(s[r])
            r+=1
        # print(stack)
        if stack:
            for l in stack:
                res+=hashmap[int(l)]
        return res
        