class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        #reverse
        for i in range(len(matrix)):
            matrix[i].reverse()