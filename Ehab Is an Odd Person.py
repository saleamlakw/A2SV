x=int(input())
y=[int(i) for i in input().split()]
even=0
odd=0
for i in y:
    if i%2:
        odd=1
    else:
        even=1
if even and odd:
    print(*sorted(y))
else:
    print(*y)
