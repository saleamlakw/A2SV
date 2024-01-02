class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r,c=len(matrix),len(matrix[0])
        transposed_matrix=[[0]*r for _ in range(c)]
        for row in range(r):
            for col in range(c):
                transposed_matrix[col][row]=matrix[row][col]
        return transposed_matrix