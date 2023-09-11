class Solution:
    def check(self,left ,right):
        l=Counter(left)
        r=Counter(right)
        for i in left:
            if i not in r or l[i]!=r[i]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=deque()
        l=0
        k=len(s1)
        for r in range(len(s2)):
            window.append(s2[r])
            while r-l+1>k:
                window.popleft()
                l+=1
            if r-l+1==k:
                if self.check(s1,s2[l:r+1]):
                    return True
        return False