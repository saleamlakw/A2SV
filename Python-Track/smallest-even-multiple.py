class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcf(n,m):
            if m==0:
                return n
            return gcf(m,n%m)
        
        hcf=gcf(max(n,2),min(n,2))
        return (n*2)//hcf