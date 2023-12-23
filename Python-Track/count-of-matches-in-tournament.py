class Solution:
    def numberOfMatches(self, n: int) -> int:
        match=0
        while n!=1:
            
            if n%2==0:
                match+=n//2
                n=n//2
            else:
                match+=((n-1)//2)+1
                n=(n-1)//2
        return match