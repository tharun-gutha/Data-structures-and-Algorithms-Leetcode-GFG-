'''class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if(matrix[i][j]==0):
                    for a in range(0,len(matrix)):
                        if(matrix[a][j]!=0): matrix[a][j]='a' 
                    for b in range(0,len(matrix[0])):
                        if(matrix[i][b]!=0): matrix[i][b]='a'
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if(matrix[i][j]=='a'):
                    matrix[i][j]=0
     #this solution has no extra memory required
     #but time complexity is more o(n^3)
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len=len(matrix)
        col_len=len(matrix[0])
        row_zero=False
        for i in range(0,row_len):
            for j in range(0,col_len):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                         matrix[i][0]=0
                    else:
                         row_zero=True
        for i in range(1,row_len):
            for j in range(1,col_len):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for i in range(0,row_len):
                matrix[i][0]=0
        if row_zero:
            for j in range(0,col_len):
                matrix[0][j]=0
                     
# the memory required is o(1)
# time complexity is o(n^2)



