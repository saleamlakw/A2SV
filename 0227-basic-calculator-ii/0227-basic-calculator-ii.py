class Solution:
    def calculate(self, s: str) -> int:
        def clean(s):
            re=[]
            i=0
            while i<len(s):
                if i<len(s) and s[i]==" ":
                    i+=1
                elif s[i] in "+-*/":
                    re.append(s[i])
                    i+=1
                else:
                    nu=""
                    while i<len(s) and s[i].isnumeric():
                        nu+=s[i]
                        i+=1
                    if nu:
                        re.append(nu)
            # print(re)
            return re
        def infToPost(s):
            stack=[]
            postfix=[]
            priority={"(":0,"+":1,"-":1,"*":2,"/":2}
            for t in s:
                if t =="(":
                    stack.append(t)
                elif t==")":
                    while stack and stack[-1]!="(":
                        postfix.append(stack.pop())
                    stack.pop()
                elif t in "+-*/":
                    while stack and priority[stack[-1]]>=priority[t]:
                        postfix.append(stack.pop())
                    stack.append(t)
                else:
                    postfix.append(t)
            while stack:
                postfix.append(stack.pop())
            # print(postfix)
            return postfix
        def infEval(s):
            import operator
            stack=[]
            op={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
            for t in s:
                if t in op:
                    b=stack.pop()
                    a=stack.pop()
                    result=op[t](a,b)
                    stack.append(int(result))
                else:
                    stack.append(int(t))
            # print(stack)
            result=""
            return stack[0]
        res=clean(s)
        post=infToPost(res)
        return infEval(post)