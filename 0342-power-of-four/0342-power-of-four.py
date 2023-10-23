class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        from math import log
        if n>0:
                b=log(n,4)
                print(b)
                if int(b)==b:
                    return True
                else:
                    return False
        else:
               return False

        