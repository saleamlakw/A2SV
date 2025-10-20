class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for start, end in intervals:
            if stack and stack[-1][1] >= start:
                stack[-1][0] = min(stack[-1][0],start)
                stack[-1][1] = max(stack[-1][1],end)
            else:
                stack.append([start,end])
        return stack
