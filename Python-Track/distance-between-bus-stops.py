class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        re=0
        for r in range(min(start,destination),max(start,destination)):
            re+=distance[r]
            distance[r]=0
        return min(re,sum(distance)) 
        