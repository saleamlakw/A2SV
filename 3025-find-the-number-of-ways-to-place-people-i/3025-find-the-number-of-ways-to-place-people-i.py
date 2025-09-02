class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0
        for i in range(n):
            ax = points[i][0]
            ay = points[i][1]
            for j in range(n):
                bx = points[j][0]
                by = points[j][1]
                flag = True
                if i != j and((bx>ax and ay>by) or (bx==ax and ay>by) or 
                    (bx>ax and ay==by)) :
                    for k in range(n):
                        cx = points[k][0]
                        cy = points[k][1]
                        if k==i or  k==j:
                            continue 
                        # print(ax,ay,bx,by,cx,cy,k==i or k==j or (ax<=cx<=bx and by<=cy<=ay))
                        if (ax<=cx<=bx and by<=cy<=ay):
                            flag = False
                            break
                    

                    if flag:
                        # print(ax,ay,bx,by,cx,cy,"flag",flag)
                        count += 1
        return count



        