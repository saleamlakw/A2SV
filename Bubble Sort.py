n=int(input())
li=[int(i) for i in input().split()]
swap=0
for i in range(n):
    for j in range(n-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            swap+=1
print(f"Array is sorted in {swap} swaps.")
print(f"First Element: {li[0]}")
print(f"Last Element: {li[-1]}")
