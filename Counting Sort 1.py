x=int(input())
y=[int(i) for i in input().split()]
t=[]
for k in range(100):
    t.append(y.count(k))
print(*t)
