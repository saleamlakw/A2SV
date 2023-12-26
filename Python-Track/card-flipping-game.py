class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        re=set()
        visit=set()
        for i in range(len(fronts)):
            if fronts[i]!=backs[i]:
                if fronts[i] not in visit:
                    re.add(fronts[i])
                if backs[i] not in visit:
                    re.add(backs[i])
            else:
                # print(re)
                if fronts[i] in re:
                    re.remove(fronts[i])
                visit.add(fronts[i])

        return min(re) if re else 0
