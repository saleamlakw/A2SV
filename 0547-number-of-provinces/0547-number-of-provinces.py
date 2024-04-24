           
class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]
        size = [1] * len(isConnected)
        def find(x):
            if x == root[x]:
                return x
            root[x] =find(root[x])
            return root[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    union(i,j)
        re=set()
        for ele in range(len(isConnected)):
            re.add(find(ele))
        return len(re)

