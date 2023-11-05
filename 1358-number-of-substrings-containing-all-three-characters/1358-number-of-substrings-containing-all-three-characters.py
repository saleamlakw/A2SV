class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        window=deque()
        result=0
        co=Counter()
        for i,r in enumerate(s):
            window.append((i,r))
            co[r]+=1
            # print(window)
            # print(co)
            while co["a"]>=1 and co["b"]>=1 and co["c"]>=1:
                result+=1
                result+=(len(s)-window[-1][0]-1)
                co[window.popleft()[1]]-=1
        return result