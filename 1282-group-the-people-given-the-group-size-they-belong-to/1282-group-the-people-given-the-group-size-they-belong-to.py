class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap=defaultdict(lambda:[[]])
        for i,val in enumerate(groupSizes):
            if len(hashmap[val][-1])==val:
                hashmap[val].append([i])
            else:
                hashmap[val][-1].append(i)
        # print(hashmap)
        res=[]
        for ele in hashmap:
            res.extend(hashmap[ele])
        return(res)