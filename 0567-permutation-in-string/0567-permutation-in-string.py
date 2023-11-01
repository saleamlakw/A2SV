class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check(left,right):
            leftCount=Counter(left)
            rightCount=Counter(right)
            for i in leftCount:
                if leftCount[i]!=rightCount[i]:
                    return False
            return True
        window=deque()
        for r in s2:
            window.append(r)
            while len(window)>len(s1):
                window.popleft()
            # print(window)
            if len(window)==len(s1) :
                if check(s1,window):
                    return True
        return  False
                