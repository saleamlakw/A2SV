class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        al=defaultdict(list)
        for kk in paths:
            re=list(kk.split(" "))
            direct=re[0]
            for j in re[1:]:
                j=j.split(".txt")
                name=j[0]
                content=j[1]
                al[content].append(direct+"/"+name+".txt")   
        a=sorted(list(al.values()))[::-1]
        return list(filter(lambda x:len(x)>1,a))
            

            
