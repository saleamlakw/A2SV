class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        visited=set()
        if "0000" in deadends:
            return -1
        else:
            queue=deque(["0000"])
        level=0
        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()
                if node==target:
                    return level

                le=node[:]
                for i in range(4):
                    if int(le[i])<9:
                        k=int(le[i])+1
                    else:
                        k=1
                    re=le[:i]+str(k)+le[i+1:]
                   
                    if re not in visited and re not in deadends:
                        queue.append(re)
                        visited.add(re)
                    if int(le[i])>=1:
                        h=int(le[i])-1
                    else:
                        h=9
                    re2=le[:i]+str(h)+le[i+1:]
                     
                    if re2 not in visited and re2 not in deadends:
                        queue.append(re2)
                        visited.add(re2)
                        

            level+=1
        return -1
