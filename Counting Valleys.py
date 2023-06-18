x=int(input())
s=input()
valley=0
ch=0
for i in s:
    if i=="D":
         ch-=1
    else:
         ch+=1
    if ch==0 and i=="U":
         valley+=1
print(valley)
