class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output=[]
        start_row=start_col=0
        end_row=len(matrix)
        end_col=len(matrix[0])
        while start_row<end_row or start_col<end_col:  # to maintain the loop within the matrix 

            if start_row<end_row :  # to move from left to right 
                for i in range(start_col,end_col):
                     output.append(matrix[start_row][i])
                start_row+=1    

            if start_col<end_col:  # to move from top to bottom
                for i in range(start_row,end_row):
                     output.append(matrix[i][end_col-1])
                end_col-=1

            if start_row<end_row:  # to move from right to left
                for i in range(end_col-1,start_col-1,-1):
                     output.append(matrix[end_row-1][i])
                end_row-=1

            if start_col<end_col:  # to move from bottom to top
                for i in range(end_row-1,start_row-1,-1):
                     output.append(matrix[i][start_col])
                start_col+=1
         
        
        return output
            
        
