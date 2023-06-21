class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        a=defaultdict(list)
        result=[]
        for i in cpdomains:
            i=i.split(" ")
            num=i[0]
            al=i[1].split(".")
            for j in range(len(al)):
                re=".".join(al[j:])
                a[re].append(int(num))
        # print(a)
        for k in a:
            result.append(str(sum(a[k]))+" "+k)
        return result
