class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(val),count) for val,count in Counter(s).items()]
        heapq.heapify(heap)

        ans = []
        while heap:

            val,fre = heapq.heappop(heap)
            use = min(repeatLimit,fre)
            ans.append(chr(-val)*use)
            
            if fre > use and heap:
                nxtVal , nxtFre = heapq.heapreplace(heap,(val,fre - use))
                ans.append(chr(-nxtVal))
                if nxtFre > 1:
                    heapq.heappush(heap,(nxtVal,nxtFre-1))

        return "".join(ans)
