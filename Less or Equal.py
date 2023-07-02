x,y=[int(i) for i in input().split()]
z=[int(i) for i in input().split()]
z.sort()
if y==0:
     if (z[0]-1)>0 and (z[0]-1)<=1000000000:
          print((z[0]-1))
     else:
          print(-1)
elif x<y:
    print(-1)
elif x==y:
    if (z[-1])>=1 and (z[-1])<=1000000000:
          print((z[-1]))
    else:
          print(-1)
elif z[y]!=z[y-1]:
         if (z[y-1])>=1 and (z[y-1])<=1000000000:
            print(z[y-1])
         else:
            print(-1)
else:
     print(-1)
     

