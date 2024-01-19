class Solution(object):
    def intervalIntersection(self, firstList, secondList):
            p1 = p2 = 0
            answer = []

            while p1 < len(firstList) and p2 < len(secondList):
                intersection = [max(firstList[p1][0],secondList[p2][0]),min(firstList[p1][1],secondList[p2][1])]
                if intersection[0] <= intersection[1]:
                    answer.append(intersection)

                if firstList[p1][1] > secondList[p2][1]:
                    p2 += 1
                else:
                    p1 += 1

            return answer
        