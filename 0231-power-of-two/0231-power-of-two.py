class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not n&n-1 if n!=0 else  False