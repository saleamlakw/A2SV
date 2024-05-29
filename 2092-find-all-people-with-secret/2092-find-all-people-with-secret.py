# class Dsu:
#     def __init__(self,n):
#         self.size=[0]*(n)
#         self.parent={i:i for i in range(n)}
#     def union(self,x,y):
#         parentX=self.find(x)
#         parentY=self.find(y)
#         if parentX!=parentY:
#             if self.size[parentX]>self.size[parentY]:
#                 self.size[parentX]+=self.size[parentY]
#                 self.parent[parentY]=self.parent[parentX]
#             else:
#                 self.size[parentY]+=self.size[parentX]
#                 self.parent[parentX]=self.parent[parentY]
#     def find(self,x):
#         while x!=self.parent[x]:
#             self.parent[x]=self.parent[self.parent[x]]
#             x=self.parent[x]
#         return x
#     def is_connected(self,x,y):
#         return self.find(x)==self.find(y)
class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        # dsu=Dsu(n)
        # dsu.union(0,firstPerson)
        sec=set([0,firstPerson])
        meetings.sort(key=lambda x:x[-1])
        result=set()
        time=set()
        all=defaultdict(lambda :defaultdict(set))
        print(all)
        for x,y,t in meetings:
            all[t][x].add(y)
            all[t][y].add(x)
            time.add(t)
        time=list(time)
        time.sort()
        
        for tt in time:
           for node in all[tt]:
                if len(all[tt][node].intersection(sec))>=1:
                    sec=all[tt][node].union(sec)
                    sec.add(node)


            
            
            
           
            
        # if 0 not in result:
        #     result.add(0)
        # if firstPerson not in result:
        #     result.add(firstPerson)    
        return list(sec)
