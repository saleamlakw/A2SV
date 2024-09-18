class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness=[-1*i for i in happiness]
        heapify(happiness)
       
        i=0
        ans=0
        while k:
            ans+=max(0,(-1*heappop(happiness))-i)
            i+=1
            k-=1
        return ans
