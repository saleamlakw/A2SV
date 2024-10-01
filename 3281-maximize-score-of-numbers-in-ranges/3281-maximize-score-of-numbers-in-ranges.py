class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def check(m):
            
            temp=start[:]
            for i in range(1,len(start)):
                if (temp[i]-temp[i-1])<m:
                    kk=m-(temp[i]-temp[i-1])
                    # print("kk",kk)
                    if kk>d:
                        return False
                    temp[i]+=kk
                # print(temp)
            return True
        l=0
        r=10**10

        start.sort()
        ans=float("-inf")
        while r>=l:
            m=(l+r)//2
            if check(m):
                # print("m",m)
                ans=max(ans,m)
                l=m+1
            else:
                r=m-1
        return ans