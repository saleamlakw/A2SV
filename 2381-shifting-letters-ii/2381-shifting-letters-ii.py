class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ru=[0]*len(s)

        for start,end,shift in shifts:
            ru[start]+=((2*shift)-1)
            if end+1<len(s):
                ru[end+1]-=((2*shift)-1)
        
        for i in range(1,len(s)):
            ru[i]+=ru[i-1]
       
        ans=[]
        for i in range(len(s)):
           ans.append(chr((ord(s[i])+ru[i]-ord("a"))%26+ord("a")))
        return "".join(ans)
