class Solution:
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
     



