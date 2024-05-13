class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {i:i for i in range(len(stones))}
        size={i:0 for i in range(len(stones))}
        def find(x):
                while x!=parent[x]:
                    parent[x]=parent[parent[x]]
                    x=parent[x]
                return x
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX!= parentY:
                if size[parentX] > size[parentY]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]
        def is_connected(x,y):
            return find(x)==find(y)
        
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    union(i,j)
        re=set()
        for ele in range(len(stones)):
            re.add(find(ele))
        return len(stones)-len(re)
    