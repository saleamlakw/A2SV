class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        all=[]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                point1=points[i]
                point2=points[j]
                distance = abs(point1[0]-point2[0])+abs(point1[1]-point2[1])
                all.append([distance,i,j])
        all.sort()


        parent = {i:i for i in range(len(points))}
        rank={i:0 for i in range(len(points))}
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

        min_weight=0
        min_edge=0
        for w,u,v in all:
            if union(u,v):
                min_weight+=w
                min_edge+=1
            if min_edge>=len(points)-1:
                break
        return min_weight
