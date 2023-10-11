class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        ma=0
        l,r=0,1
        print(points)
        while r<len(points):
            ma=max(ma,(points[r][0]-points[l][0]))
            l+=1
            r+=1
        return ma
            