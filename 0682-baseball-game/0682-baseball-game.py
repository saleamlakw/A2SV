class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for s in operations:
            if s=="+":
                if len(stack)>=2:
                    b=stack[-1]
                    a=stack[-2]
                    stack.append(a+b)
            elif s=="D":
                if stack:
                    stack.append(stack[-1]*2)
            elif s=="C":
                if stack:
                    stack.pop()
            else:
                 stack.append(int(s))
        return sum(stack)