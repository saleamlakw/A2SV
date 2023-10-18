class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        stack=[]
        re=0
        operators={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
        for i in tokens:
            if stack and i in "+-*/":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(int(operators[i](b,a)))
            else:
                stack.append(i)
        return int(stack[0])