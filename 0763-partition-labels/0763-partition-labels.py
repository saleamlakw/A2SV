class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        visit=set()
        co=Counter(s)
        l=0
        re=0
        result=[]
        for r in range(len(s)):
            if s[r] not in visit:
                re+=(co[s[r]]-1)
                visit.add(s[r])
            else:
                re-=1
            if re==0:
                result.append(r-l+1)
                l=r+1
        return result
            
                
                
                
            