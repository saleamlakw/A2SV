class Solution:
    from collections import defaultdict
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1]))
        if capacity>=trips[0][0]:
            capacity-=trips[0][0]
            tri=defaultdict(list)
            tri[trips[0][0]].append(trips[0][2])
        else:
            return False
        for k,a,b in trips[1:]:
            if capacity>=k:
                capacity-=k
                tri[k].append(b)
            else:
                k-=capacity
                r=0
                po=[]
                for j in tri:
                    tri[j].sort(reverse=True)
                    while tri[j] and tri[j][-1]<=a:
                        r+=j
                        tri[j].pop()
                if r>=k: 
                    tri[k+capacity].append(b)
                    capacity=r-k
                else:
                    return False
        return True
                        
                
            
            
            
        