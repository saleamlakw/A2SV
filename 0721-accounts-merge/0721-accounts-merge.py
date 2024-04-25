class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        cc=Counter()
        parent = {}
        g=defaultdict(set)
        for acc in accounts:
            parent[acc[0]+str(cc[acc[0]])]=acc[0]+str(cc[acc[0]])
            g[acc[0]+str(cc[acc[0]])]=set(acc[1:])
            cc[acc[0]]+=1
        # print(parent)
        # print(g)
        rank={i:0 for i in g}
        # print(rank)
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            # print("++++",parentX,parentY)
            if parentX != parentY:
                if rank[parentX]>rank[parentY]:
                    parent[parentY]=parentX
                elif rank[parentX]<rank[parentY]:
                    parent[parentX]=parentY
                elif rank[parentX]==rank[parentY]:
                     parent[parentX]=parentY
                     rank[parentY]+=1
                # print("---",parentX,parentY,parent)

        # print(g)
        for ele1 in g:
            for ele2 in g:
                # print(ele1,ele2,len(g[ele1].intersection(g[ele2]))>=1 and  ele1!=ele2,g[ele1],g[ele2])
                if len(g[ele1].intersection(g[ele2]))>=1 and  ele1!=ele2:
                    union(ele1,ele2)
        
        # print(parent)
        result=defaultdict(list)

        for elef in g:
            par=find(elef)
            # print(elef,par)
            result[par]=list(result[par])+list(g[elef])
        # print(result)
        rc=[]
        for cv in result:
            nameonly=""
            for com in cv:
                if not com.isdigit():
                     nameonly+=com
            oup=[nameonly,*list(sorted(list(set(result[cv]))))]
            rc.append(oup)
        return (rc)
        
                   