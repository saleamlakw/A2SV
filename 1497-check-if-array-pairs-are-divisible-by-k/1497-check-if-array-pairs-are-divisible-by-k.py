class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod=[]
        co=0
        for ele in arr:
            m=ele%k
            if m==0:
                co+=1
            else:
                mod.append(m)
        mod.sort()
        print(mod)
        l=0
        r=len(mod)-1
        if len(mod)%2!=0:
            return False
        while r>l:
            if mod[l]+mod[r]!=k:
                return False
            l+=1
            r-=1
        return True

