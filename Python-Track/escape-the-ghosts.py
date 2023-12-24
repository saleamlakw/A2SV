class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for r in ghosts:
            # if (0<abs(r[0]) and abs(r[0])<=abs(target[0])) or (0<abs(r[1]) and abs(r[1])<=abs(target[1])):
            #     return False
            if (abs(r[0]-target[0])+abs(r[1]-target[1]))<=(abs(target[0])+abs(target[1])):
               return False
        return True

        