class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre=[0]*n
        current=[0]*n
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    current[j]=1
                    continue
                up=pre[j] if i>0 else 0
                left=current[j-1] if j>0 else 0
                current[j]=up+left
            pre=current[:]
            current=[0]*n
        return pre[n-1]
       
            