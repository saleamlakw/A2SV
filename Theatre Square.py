n,m,a=[int(i) for i in input().split()]
from math import ceil
re=ceil(n/a)
re2=ceil(m/a)*re
print(re2)
