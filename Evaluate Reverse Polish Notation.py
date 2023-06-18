class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        operators={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
        stack=[]
        for i,val in enumerate(tokens):
             if  stack and val in "+-*/":
                 a=stack.pop()
                 b=stack.pop()
                 stack.append(int(operators[val](b,a)))
             else:
                 stack.append(int(val))
        return stack[0]
