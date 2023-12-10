class Solution(object):
    def appendCharacters(self, s, t):
        hashmap=Counter(t)
        indhash=defaultdict(deque)
        for i in range(len(s)):
            if s[i] in hashmap:
                indhash[s[i]].append(i)
        
        
        def check(c,r,h):
            if c in h:
                while h[c]:
                    if h[c][0]>r:
                      
                        return [True,h[c][0]]
                    else:
                        h[c].popleft()
                    
                        
            return []
        
        ans=len(t)
        r=0
        while r < len(s):
            if s[r]==t[0]:
                l=1
                ans=min(ans,len(t)-l)
                while r < len(s) and l<len(t) and  (u := check(t[l],r,indhash)):
                    ans=min(ans,len(t)-l-1)
                    r=u[1]
                    # print(r,"r")
                    l+=1
            r+=1
        return ans