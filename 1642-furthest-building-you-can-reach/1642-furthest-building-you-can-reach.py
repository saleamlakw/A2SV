class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff=[]
        for h in range(len(heights)-1):
            if heights[h+1]>heights[h]:
                diff.append(heights[h+1]-heights[h])
            else:
                diff.append(0)

        def bs(m):
            bricks_needed=sum(diff[:m])
            temp=sorted(diff[:m])
            for _ in range(ladders):
                if bricks_needed==0:
                    break
                bricks_needed-=temp.pop()
            return bricks>=bricks_needed

        l=0
        r=len(heights)-1
        result=float("-inf")
        while l<r:
            m=(l+r)//2
            if bs(m):
                l=m+1
                result=max(result,m+1)
            else:
                r=m-1
        return result if bs(result) else result-1
        

       