class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        all=[]
        for i in range(len(positions)):
            all.append([positions[i],directions[i],i])
            
        all.sort()
        stack=[]
        for j in range(len(all)):
            #print(j,stack)
            if stack:
                if all[j][1]=="L":
                    
                    while stack and stack[-1][1]=="R":
                        poped=stack.pop()
                        if healths[poped[2]]>healths[all[j][2]]:
                            healths[poped[2]]-=1
                            healths[all[j][2]]=0
                            stack.append(poped)
                            break
                        elif healths[poped[2]]<healths[all[j][2]]:
                            healths[poped[2]]=0
                            healths[all[j][2]]-=1
                        else:
                            healths[poped[2]]=0
                            healths[all[j][2]]=0
                            break                    
                else:
                    stack.append(all[j])
            else:
                stack.append(all[j])
        return [x for x in healths if x>0]
        