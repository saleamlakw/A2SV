class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr=[0]*len(s)
        for l,r,d in shifts:
            k=2*d-1
            arr[l]+=k
            if r+1<len(s):
                arr[r+1]-=k
        arr=list(accumulate(arr))
        result=[]
        for i in range(len(s)):
            re=chr((((ord(s[i])+arr[i])-ord("a"))%26)+ord("a"))
            result.append(re)
        return "".join(result)