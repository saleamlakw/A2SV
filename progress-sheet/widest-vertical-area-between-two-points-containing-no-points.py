class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        re=float("-inf")
        # print(points)
        for i in range(1,len(points)):
            re=max(re,points[i][0]-points[i-1][0])
        return re