class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a=0
        b=0
        d=deque()
        for i in colors:
            d.append(i)
            while(len(d)>3):
                d.popleft()
            if len(d)==3 and len(set(d))==1:
                if d[0]=='A':
                    a+=1
                else:
                    b+=1
        return a>b
           
            