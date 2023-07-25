class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       l,r=1,max(piles)
       res=r
       def check(k):
           hour=0
           for j in piles:
               if j//k==0:
                   hour+=1
               elif j%k==0:
                    hour+=j//k
               else:
                    hour+=(j//k)+1
           return hour<=h
       while l<=r:
           k=(l+r)//2
           if check(k):
               res=min(res,k)
               r=k-1
           else:
               l=k+1
       return res
