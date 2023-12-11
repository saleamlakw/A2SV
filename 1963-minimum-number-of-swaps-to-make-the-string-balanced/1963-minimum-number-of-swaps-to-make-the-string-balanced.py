class Solution:
    def minSwaps(self, s: str) -> int:
        ans=0
        for r in s:
            if r=="[":
                ans+=1
            else:
                if ans:
                    ans-=1
        return (ans+1)//2