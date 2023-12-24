class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        re=0
        for r in range(0,len(points)-1):
            re+=max(abs(points[r+1][0]-points[r][0]),abs(points[r+1][1]-points[r][1]))
        return re