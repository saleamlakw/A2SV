class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        a=capacityA
        b=capacityB
        left=0
        right=len(plants)-1
        res=0
        while left<=right:
            ch=True
            if left ==right:
                if capacityA==capacityB:
                    if capacityA>=plants[left]:
                        capacityA-=plants[left]
                        left+=1
                    else:
                        capacityA=a
                        capacityA-=plants[left]
                        left+=1
                        res+=1
                        ch=False
                else:
                    if capacityA>capacityB:
                        if capacityA>=plants[left]:
                            capacityA-=plants[left]
                            left+=1
                        else:
                            capacityA=a
                            capacityA-=plants[left]
                            left+=1
                            res+=1
                            ch=False
                    else:
                        if capacityB>=plants[right]:
                            capacityB-=plants[right]
                            right-=1
                        else:
                            capacityB=b
                            capacityB-=plants[right]
                            right-=1
                            res+=1
                            ch=False
            else:
                if capacityA>=plants[left]:
                    capacityA-=plants[left]
                    left+=1
                else:
                    capacityA=a
                    capacityA-=plants[left]
                    left+=1
                    res+=1
                    ch=False
                if capacityB>=plants[right]:
                        capacityB-=plants[right]
                        right-=1
                else:
                        capacityB=b
                        capacityB-=plants[right]
                        right-=1
                        res+=1
                        ch=False
        return res