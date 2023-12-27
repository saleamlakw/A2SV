class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap=Counter()
        for ele in cpdomains:
            count,domain=ele.split()
            subDomain=domain.split(".")
            for i in range(len(subDomain)):
                hashmap[".".join(subDomain[i:])]+=int(count)
        result=[]
        for re in hashmap:
            result.append(str(hashmap[re])+" "+str(re))
        return result