#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        stack=[]
        postfix=[]
        priority={"(":0,"+":1,"-":1,"*":2,"/":2,"^":3}
        for t in exp:
            if t=="(":
                stack.append(t)
            elif t==")":
                while stack and stack[-1]!="(":
                    postfix.append(stack.pop())
                stack.pop()
            elif t in "+-*/^":
                while stack and priority[stack[-1]]>=priority[t]:
                    postfix.append(stack.pop())
                stack.append(t)
            else:
                postfix.append(t)
        while stack:
            postfix.append(stack.pop())
        return "".join(postfix)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends