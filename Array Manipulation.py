def arrayManipulation(n, queries):
    arr=[0]*(n+2)
    for a,b,k in queries:
        arr[a]+=k
        arr[b+1]-=k
    su=0
    ma=0
    for i in arr:
         su+=i
         ma=max(ma,su)
    return ma
