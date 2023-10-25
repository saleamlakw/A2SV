class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        def merge(l,r):
            if l[1]>=r[0]:
                return [l[0],max(l[1],r[1])]
            return [l,r]
        if len(intervals)==1:
            return intervals
        re=[]
        left=intervals[0]
        for i in range(1,len(intervals)):
            left=merge(left,intervals[i])
            a=left[0]
            if isinstance(a, int):
                if re:
                    re.pop()
                re.append(left)
            else:
                if re and left[0]==re[-1]:
                    re.append(left[1])
                else:
                    re=re+left
                left=left[1]
            # print(re)
        return re
            