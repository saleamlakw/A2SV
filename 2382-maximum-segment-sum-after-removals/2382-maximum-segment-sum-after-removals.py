class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        a=nums
        b=removeQueries[::-1]
        n=len(nums)
        result=[]
        switch=[False]*n
        tot=[0]*n
        parent = {i:i for i in range(n)}
        rank={i:0 for i in range(n)}
        maxr=0
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            nonlocal maxr
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                if rank[parentX]>rank[parentY]:
                    parent[parentY]=parentX
                    tot[parentX]+=tot[parentY]
                    # debug("--".tot[x])
                    # maxr=max(maxr,tot[x])
                elif rank[parentX]<rank[parentY]:
                    parent[parentX]=parentY
                    tot[parentY]+=tot[parentX]
                elif rank[parentX]==rank[parentY]:
                        parent[parentX]=parentY
                        rank[parentY]+=1
                        tot[parentY]+=tot[parentX]
                        
    
        for i in range(n):
            result.append(maxr)
            switch[b[i]]=True
            tot[b[i]]+=a[b[i]]
            
            if (b[i]-1)>=0 and switch[b[i]-1]==True:
                union(b[i],b[i] - 1)
            if (b[i]+1)<n and switch[b[i]+1]==True:
                union(b[i],b[i]+1)
            maxr=max(maxr,tot[find(b[i])])
        return (result[::-1])
  