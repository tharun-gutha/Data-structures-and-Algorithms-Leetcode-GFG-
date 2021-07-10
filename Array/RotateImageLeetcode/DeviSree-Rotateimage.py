class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for i in range(len(matrix)): 
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]  # here the matrix is transposed
     
        for i in range(len(matrix)):
            for j,k in zip(range(len(matrix)),range(len(matrix)-1,-1,-1)):
                if j<=k:
                    matrix[i][j],matrix[i][k]=matrix[i][k],matrix[i][j] # reversing the elements position in the row
                
        """
        Do not return anything, modify matrix in-place instead.
        """
        