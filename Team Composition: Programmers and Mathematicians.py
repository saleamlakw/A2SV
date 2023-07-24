x=int(input())
for _ in range(x):
    y,z=[int(i) for i in input().split()]
    if ((y+z)//4)<=min(y,z):
        print((y+z)//4)
    else:
        print(min(y,z))
    
