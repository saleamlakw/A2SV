class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result=[]
        cc=Counter()
        pp=Counter(p)
        l=0
        for r in range(len(s)):
            cc[s[r]]+=1
            while r-l+1>len(p):
                cc[s[l]]-=1
                if cc[s[l]]==0:
                    cc.pop(s[l])
                l+=1
            if r-l+1==len(p):
               
                if cc==pp:
                    result.append(l)
                    
        return result
