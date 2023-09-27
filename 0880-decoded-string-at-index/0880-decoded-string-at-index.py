class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total=0
        for i  in s:
            if i.isnumeric():
                total*=int(i)
            else:
                total+=1
        for h in reversed(s):
            k%=total
            if k==0 and h.isalpha():
                return h
            if h.isnumeric():
                total/=int(h)
            else:
                total-=1
        
    
        