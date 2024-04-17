class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks.sort()
        all=[]
        for i in range(len(tasks)):
            all.append([tasks[i][0],i,tasks[i][1]])
        # print(all)
        all.sort()
        tottime=all[0][0]
        k=0
        heap=[]
        ans=[]

        while k<len(all):
            while k<len(all) and all[k][0]<=tottime:
                heappush(heap,[all[k][2],all[k][1],all[k][0]])
                k+=1
            # print(heap,tottime)
            if heap:
                pr,ind,sta=heappop(heap)
                ans.append(ind)
                tottime+=pr
            else:
                tottime=all[k][0]
        while heap:
            pr,ind,sta=heappop(heap)
            ans.append(ind)

        return ans
