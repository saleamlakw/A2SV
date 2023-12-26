class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumSquares(n):
            re=0
            while n!=0:
                re+=((n%10)**2)
                n//=10
            return re
        visited=set()
        while n!=1:
            val=sumSquares(n)
            if val in visited:
                return n==1
            visited.add(val)
            n=val
        return n==1

        