class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        all=[]
        for r in points:
            all.append([r,math.sqrt(r[0]**2+r[1]**2)])
        
        all.sort(key=lambda x: x[1])
        print(all)
        return [all[i][0] for i in range(k)]