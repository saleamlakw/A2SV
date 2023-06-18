class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        from math import log ,isclose
        if n>0:
                b=math.log10(n) / math.log10(3)
                print(b)
                if b==int(b):
                    return True
                else:
                    return False
        else:
               return False  
        
