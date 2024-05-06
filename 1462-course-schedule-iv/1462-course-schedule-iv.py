class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph=defaultdict(list)
        ind=[0]*numCourses

        for u,v in prerequisites:
            graph[u].append(v)
            ind[v]+=1

        queue=deque()
        for node in range(numCourses):
            if ind[node]==0:
                queue.append([node,0])
        
        order=[]
        while queue:
            node,level=queue.popleft()
            order.append([node,level])

            for nb in graph[node]:
                ind[nb]-=1

                if ind[nb]==0:
                    queue.append([nb,1])
        
        result=defaultdict(list)

        ind=0
        # group=0

        print(order)
        for ele in order:
            result[ele[0]]=[ind,ele[1]]
            # if ele[1]==0:
            #     group+=1
            #     ind=0
            #     result[ele[0]]=[ind,group]
            # else:
            #     result[ele[0]]=[ind,group]
            ind+=1
        print(result)
        ans=[]

        for a,b in queries:
            if result[a][1]==0 and result[b][1]==0:
                ans.append(False)
            else:
                if result[a][0]<result[b][0]:
                    ans.append(True)
                else:
                    ans.append(False)
            
        return ans


            

