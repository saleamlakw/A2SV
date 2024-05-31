class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree=[0]*n
        graph=defaultdict(list)

        for pre,cor in relations :

            graph[pre].append(cor)
            indegree[cor-1]+=1

        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append([i+1,time[i]])
       
        result=0
        mx=0
        hashmap=Counter()
        while queue:
            print(queue)
            for _ in range(len(queue)):
                node,month=queue.popleft()
                mx=max(mx,month)
                if graph[node]:
                    mx=max(mx,time[node-1])
                for nb in graph[node]:
                    hashmap[nb]=max(hashmap[nb],month)
                    indegree[nb-1]-=1
                    if indegree[nb-1]==0:
                        queue.append([nb,hashmap[nb]+time[nb-1]])
          
     
        
        return mx
        