class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window=deque()
        co=Counter()
        re=0
        for r in s:
            window.append(r)
            co[r]+=1
            while len(window)-max(co.values())>k:
                co[window.popleft()]-=1
            re=max(re,len(window))
        return re
            