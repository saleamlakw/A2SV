class Solution:
    def maxProfitAssignment(self, d: List[int], p: List[int], w: List[int]) -> int:
        task = list(zip(d, p))
        t = sorted(task, key=lambda x:-x[1])
        w.sort(reverse=True)
        profit = 0
        i = 0
        j = 0
        while i < len(w) and j < len(t):
            if w[i] < t[j][0]:
                j += 1
            else:
                profit += t[j][1]
                i += 1 
        return profit