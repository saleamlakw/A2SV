class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter() 
        co = Counter()
        for i in range(len(s)):
            co[ord(s[i])]+=1
        heap = [(-c,co[c])for c in co]
        heapq.heapify(heap)

        ans = []
        pre = -1
        while heap:
            
            val,fre = heapq.heappop(heap)
            val = -val
            # print(val,pre)
            if pre == val:
                if count[val] < repeatLimit:
                    ans.append(chr(val))
                    count[val] += 1
                    if fre - 1>0:
                        heapq.heappush(heap,(-val,fre-1))
                else:
                    if heap:
                        poped2,fre2 = heapq.heappop(heap)
                        poped2 = -poped2
                        ans.append(chr(poped2))
                        if fre2 - 1>0:
                            heapq.heappush(heap,(-poped2,fre2-1))
                        heapq.heappush(heap,(-val,fre))
                        count = Counter()
                        count[poped2]+=1
                        pre = poped2

            else:
                # print("--",val)
                ans.append(chr(val))
                count = Counter()
                count[val]+=1
                if fre - 1>0:
                    heapq.heappush(heap,(-val,fre-1))
            pre = val
        return "".join(ans)
