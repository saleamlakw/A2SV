x=int(input())
for _ in range(x):
    y=int(input())
    z=[int(i) for i in input().split()]
    z.sort()
    stack=[]
    for k in z:
        if stack and (k-stack[-1]) in [0,1]:
            stack.pop()
        stack.append(k)
    if len(stack)==1:
        print("YES")
    else:
        print("NO")
