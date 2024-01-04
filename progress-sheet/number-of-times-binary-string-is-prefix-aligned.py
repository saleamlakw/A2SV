class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        al=list(range(2,len(flips)+1))
        result=0
        min0=1
        max1=float("-inf")
        visit=set([1])
        for f in flips:
            visit.add(f)
            if min0==f:
                if al:x=heapq.heappop(al)
                else:
                    x=-1
                # print("al",al)
                # print(x,"x")
                # print(visit,"visit")
                while al and x in visit  :
                    x=heapq.heappop(al)
                    # print(visit,"visit")
                    # print(x,"x")
                    # print("al",al)
                if x!=-1:
                    min0=x
                visit.add(min0)
            max1=max(max1,f)
            # print(min0,max1)
            if min0>max1:
                result+=1
        return result+1

