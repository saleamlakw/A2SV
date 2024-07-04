class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        all=[]
        for i in range(len(costs)):
            all.append([costs[i][0],costs[i][1],costs[i][0]-costs[i][1]])
        all.sort(key=lambda x:x[-1],reverse=True)
        res=0

        for j in range(len(costs)):
            if j<(len(costs)//2):
                res+=all[j][1]
            else:
                res+=all[j][0]
        return res