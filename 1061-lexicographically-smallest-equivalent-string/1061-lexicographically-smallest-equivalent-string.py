class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #with iterrative path compression 
        al=list(set(s1+s2))
        root = {i:i for i in al }
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rootX < rootY:
                    root[rootY] = rootX
                else:
                    root[rootX] = rootY
        remin="z"
        for i in range(len(s1)):
            union(s1[i],s2[i])
        result=[]
        for ele in baseStr :
            if ele in root:
                while ele !=root[ele]:
                    ele=root[ele]
                result.append(root[ele])
            else:
                result.append(ele)
        return "".join(result)

        
