class Solution:
    def reverse(self, x: int) -> int:
        y=str(x)
        if int(y)>=0:
            z=int(y[::-1])
        else:
            f=y[1:]
            z=-1*int(f[::-1])

        if z>=-2**31 and z<=(2**31)-1:
            return z 
        else:
            return 0
