class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(r,c):
            nums=[0]*10
            row_sum=set()
            col_sum=set()
            d1=0
            d2=0
            for i in range(3):
                rr=0
                cc=0
                for j in range(3):
                    if grid[r+i][c+j]>9:
                        return False
                    nums[grid[r+i][c+j]]=1
                    #print(r+i,c+j)
                    rr+=grid[r+i][c+j]
                    cc+=grid[r+j][c+i]
                    if i==j:
                        d1+=grid[r+i][c+j]
                    if i+j==2:
                        d2+=grid[r+i][c+j]
                row_sum.add(rr)
                col_sum.add(cc)
            #print(row_sum,col_sum)
            #print(nums)
            #print(d1,d2)
            return nums[0]==0 and all(nums[1:]) and len(row_sum)==1 and row_sum==col_sum and col_sum==set([d1]) and d1==d2
        ans=0
        for i in range(len(grid)):
             for j in range(len(grid[0])):
                       if i+2<len(grid) and j+2<len(grid[0]):
                            if check(i,j):
                                ans+=1
        return ans
                       
                       
                    
                
                    
                    
                