class Solution {
    public void setZeroes(int[][] matrix) {
        int rows=matrix.length,cols=matrix[0].length;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(matrix[i][j]==0){
                   matrix[0][j]=0;
                    matrix[i][0]=0;
                }
            }
            
        }
        for(int i=rows-1;i>=0;i--){
            for(int j=cols-1;j>=0;j--){
                if(matrix[i][0]==0 || matrix[0][j]==0){
                    matrix[i][j]=0;
                    
                }
            }
        }
    }
}