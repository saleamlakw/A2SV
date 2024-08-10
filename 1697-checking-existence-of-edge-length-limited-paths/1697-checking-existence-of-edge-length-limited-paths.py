class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x :x[-1])
        queries=[[i]+queries[i] for i in range(len(queries))]
        queries.sort(key=lambda x :x[-1])
        ans=[False]*len(queries)

        # print(queries)
        # print(edgeList)
        parent = {i:i for i in range(n)}
        rank={i:0 for i in range(n)}
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
        left=0
        right=0

        while left<len(queries):
            while right<len(edgeList) and edgeList[right][-1]<queries[left][-1]:
                union(edgeList[right][0],edgeList[right][1])
                right+=1
            # print(queries[left])
            if find(queries[left][1])==find(queries[left][2]):
                ans[queries[left][0]]=True
            left+=1
        return ans
