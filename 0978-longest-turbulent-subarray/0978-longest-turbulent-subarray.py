class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,r=0,1
        re=1
        sym=""
        while r<len(arr):
            if arr[r]>arr[r-1] and sym!=">":
                re=max(re,r-l+1)
                sym=">"
                r+=1
            elif arr[r]<arr[r-1] and sym!="<":
                re=max(re,r-l+1)
                sym="<"
                r+=1
            elif arr[r]==arr[r-1]:
                l=r
                r+=1
                sym=""
            else:
                l+=1
                r=l+1
                sym=""
        return re