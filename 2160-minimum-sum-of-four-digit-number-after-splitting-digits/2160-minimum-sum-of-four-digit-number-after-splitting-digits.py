class Solution:
    def minimumSum(self, num: int) -> int:
        a=list(str(num))
        a=sorted(list(map(int,a)))
        x=int(str(a[0])+str(a[2]))
        y=int(str(a[1])+str(a[3]))
        return x+y