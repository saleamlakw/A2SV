class Solution(object):
    def appendCharacters(self, s, t):
        hashmap=Counter(t)
        indhash=defaultdict(deque)
        for i in range(len(s)):
            if s[i] in hashmap:
                indhash[s[i]].append(i)
        # print(dict(indhash))
        def check(c,r,h):
            # nonlocal ll 
            # print(ll,"ll")
            if c in h:
                while h[c]:
                    if h[c][0]>r:
                      
                        return [True,h[c][0]]
                    else:
                        h[c].popleft()
                    
                        
            return []
        
        ch=len(t)
        r=0
        while r < len(s):
            if s[r]==t[0]:
                l=1
                ch=min(ch,len(t)-l)
                while r < len(s) and l<len(t) and  (u := check(t[l],r,indhash)):
                    ch=min(ch,len(t)-l-1)
                    r=u[1]
                    # print(r,"r")
                    l+=1
            r+=1
        return ch