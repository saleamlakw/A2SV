class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        per,curper=[],[]
        self.helper(1,n,k,per,curper)
        return per
    def helper(self,i,n,k,per,curper):
        if len(curper)==k:
            per.append(curper.copy())
            return
        if i>n:
            return
        for j in range(i,n+1):
            curper.append(j)
            self.helper(j+1,n,k,per,curper)
            curper.pop()
        
        
