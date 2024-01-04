class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result=0
        visited=set()
        d1r,d1c=0,0
        d2r,d2c=(0,len(mat[0])-1)
        def inbound(arr):
            return 0<=arr[0]<len(mat) and 0<=arr[1]<len(mat[0])
        while inbound((d1r,d1c)) and inbound((d1r,d1c)):
            if (d1r,d1c) not in visited:
                result+=mat[d1r][d1c]
            visited.add((d1r,d1c))
            d1r+=1
            d1c+=1
            if (d2r,d2c) not in visited:
                result+=mat[d2r][d2c]
            visited.add((d2r,d2c))
            d2r+=1
            d2c-=1
        return result