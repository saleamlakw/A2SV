from collections import defaultdict
graph=defaultdict(list)
x=int(input())
y=int(input())
for i in range(y):
    z=[int(i) for i in input().split()]
    if z[0]==1:
        graph[z[1]].append(z[2])
        graph[z[2]].append(z[1])
    elif z[0]==2:
        print(*graph[z[1]])
