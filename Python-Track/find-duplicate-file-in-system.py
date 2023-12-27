class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for e in paths:
            all=e.split()
            root=all[0]
            for f in all[1:]:
                l=f.split(".txt")
                num=l[0]
                content=l[1]
                re=root+"/"+num+".txt"
                hashmap[content].append(re)
        return [hashmap[j] for j in hashmap if len(hashmap[j])>1]
