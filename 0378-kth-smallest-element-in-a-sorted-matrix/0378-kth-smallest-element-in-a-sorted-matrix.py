class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix)<=1:
            return matrix[0][0]
        else:
            mat=matrix[0]
            for i in range(1,len(matrix)):
                mat=self.merge(mat,matrix[i])
            return mat[k-1]
    def merge(self,left,right):
            res=[]
            i=0
            j=0
            while i<len(left) and j<len(right):
                if left[i]< right[j]:
                    res.append(left[i])
                    i+=1
                else :
                    res.append(right[j])
                    j+=1
            while i<len(left):
                res.append(left[i])
                i+=1
            while j<len(right):
                res.append(right[j])
                j+=1
            return res
                
                
                
    