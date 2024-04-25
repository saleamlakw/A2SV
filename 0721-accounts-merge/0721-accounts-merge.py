class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        g=defaultdict(set)
        for ele in accounts:
            name,email=ele[0],set(ele[1:])
            ch=False
            num=0
            for ss in g:
                rename=""
                digit=""
                for n in ss:
                    if not n.isdigit():
                        rename+=n
                    else:
                        digit+=n
                digit=digit[::-1]
                # print(rename,digit)
                if rename==name:
                    num=max(num,int(digit))
                    if len(email.intersection(g[ss]))>0:
                        # print("union",email.union(g[ss]))
                        # print(email,g[ss])
                        g[ss]=email.union(g[ss])
                        ch=True
                        break
                    
            if not ch:
                # print("--",name,num,email)
                g[name+str(num+1)]=email
        #     print(g)
        # print(g)

        result=[]
        for res in g:
            rt=""
            for l in res:
                    if not l.isdigit():
                            rt+=l
            appe=[rt,*list(sorted(g[res]))]
            result.append(appe)
        return result

                   