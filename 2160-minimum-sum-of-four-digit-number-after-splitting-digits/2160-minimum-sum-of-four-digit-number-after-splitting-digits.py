class Solution:
    def minimumSum(self, num: int) -> int:
        a=list(str(num))
        a=list(map(int,a))
        a.sort()
        re=[]
        x=int(str(a[0])+str(a[2]))
        print(x)
        y=int(str(a[1])+str(a[3]))
        print(y)
        return x+y