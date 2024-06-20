class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(mid,m):
            pre=position[0]
            m-=1
            for i in range(1,len(position)):
                if m<=0:
                    break
                if position[i]-pre>=mid:
                    pre=position[i]
                    m-=1
            return m==0
        l=1
        r=max(position)*3
        res=float("-inf")
        while r>l:
            mid=(l+r)//2
            if check(mid,m):
                res=max(res,mid)
                l=mid+1
            else:
                r=mid
        return res
