class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        window=deque()
        result=0
        for r in s:
            window.append(r)
            while len(window)>3:
                window.popleft()
            # print(window)
            if len(window)==3 and len(window)==len(set(window)):
                result+=1
        return result
            
            