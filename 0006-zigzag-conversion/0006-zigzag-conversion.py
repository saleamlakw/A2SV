class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        grid=[[0]*len(s) for _ in range(numRows)]

        down=[1,0]
        updigonal=[-1,1]

        def inbound(r,c):
            return 0<=r<numRows and 0<=c<len(s)


        turn = True
        r,c=0,0
        i=0
        while i<len(s):
            while i <len(s) and inbound(r,c):
                grid[r][c]=s[i]
                if turn:
                    r+=down[0]
                    c+=down[1]
                    
                else:
                    r+=updigonal[0]
                    c+=updigonal[1]
                i+=1
            if turn:
                r-=1
                r-=1
                c+=1
            else:
                r+=1
                c-=1 
                r+=1
            turn =not turn
        
        ans=[]
        for i in range(numRows):
            for j in range(len(s)):
                if grid[i][j]!=0:
                    ans.append(grid[i][j])
        return ("".join(ans))