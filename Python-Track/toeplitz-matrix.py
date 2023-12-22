class Solution:
   def isToeplitzMatrix(self, matrix):
       for i in range(len(matrix)):
           for j in range(len(matrix[i])):
               kv=matrix[i][j]
               kk=j+1
               for k in range(i+1,len(matrix)):
                   if kk<len(matrix[k]) and matrix[k][kk]!=kv:
                       return False
                   kk+=1    
       return True 