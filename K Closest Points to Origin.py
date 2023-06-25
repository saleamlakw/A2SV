class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       from math import sqrt 
       li=[]
       for i in points:
           f=sqrt((i[1]**2)+(i[0]**2))
           li.append([i,f])
       li.sort(key=lambda x:x[1])
       result=[]
       for jj in range(k):
          result.append((li[jj][0]))
       return result
