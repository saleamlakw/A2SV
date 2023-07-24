class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def check(cap):
            ship,capcity=1,cap
            for i in weights:
                if capcity-i<0:
                    ship+=1
                    capcity=cap
                capcity-=i
            return ship<=days
        while l<=r:
            cap=(l+r)//2
            if check(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res
