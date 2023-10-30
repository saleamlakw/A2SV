class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator 
        op={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
        stack=[]
        for t in tokens:
            if t in "+-*/":
                b=stack.pop()
                a=stack.pop()
                result=op[t](a,b)
                stack.append(int(result))                                    
            else:
                stack.append(int(t))
        return stack[0]    
            
                