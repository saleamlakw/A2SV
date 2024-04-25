class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        all=[]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                point1=points[i]
                point2=points[j]
                distance = abs(point1[0]-point2[0])+abs(point1[1]-point2[1])
                all.append([distance,tuple(point1),tuple(point2)])
        all.sort()


        parent = {tuple(i):tuple(i) for i in points}
        rank={tuple(i):0 for i in points}
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                if rank[parentX]>rank[parentY]:
                    parent[parentY]=parentX
                elif rank[parentX]<rank[parentY]:
                    parent[parentX]=parentY
                elif rank[parentX]==rank[parentY]:
                        parent[parentX]=parentY
                        rank[parentY]+=1
                return True
            else:
                return False

        result=0
        for ele in all:
            if union(ele[1],ele[2]):
                result+=ele[0]
        return result
