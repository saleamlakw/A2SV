class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        al=[]
        for j in range(len(mat[0])):
            al.append((0,j))
        for i in range(1,len(mat)):
           al.append((i,len(mat[0])-1))
        # print(al)
        result=[]
        def inbound(r,c):
            return 0<=r<len(mat) and 0<=c<len(mat[0])
        for e in al:
            row=e[0]
            col=e[1]
            re=[]
            # print((row,col),inbound(row,col))
            while inbound(row,col):
                re.append(mat[row][col])
                row+=1
                col-=1
            if re :
                result.append(re)
        # print(result)

        for i in range(0,len(result),2):
            result[i]=reversed(result[i])
        ans=[]
        for ele in result:
            ans.extend(ele)
        return ans
