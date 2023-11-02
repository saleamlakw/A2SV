class Solution:
    def compress(self, chars: List[str]) -> int:
        li=deque()
        s=""
        for r in chars:
            res=0
            if li and li[-1]!=r:
                while li:
                    res+=1
                    poped=li.popleft()
                if res>1:
                    s+=(poped+str(res))
                else:
                     s+=(poped)
            li.append(r)
        if li:
            if len(li)>1:
                s+=(li[-1]+str(len(li)))
            else:
                s+=(li[-1])
        for kk in range(len(s)):
            chars[kk]=s[kk]
        return len(s)
            