x=int(input())
for i in range(x):
    n=int(input())
    if n<38:
        print(n)
    elif round(n,-1)<n:
        if ((round(n,-1)+5)-n)<3:
             print(round(n,-1)+5)
        else:
             print(n)
    else:
        if ((round(n,-1))-n)<3:
             print(round(n,-1))
        else:
             print(n)
            
