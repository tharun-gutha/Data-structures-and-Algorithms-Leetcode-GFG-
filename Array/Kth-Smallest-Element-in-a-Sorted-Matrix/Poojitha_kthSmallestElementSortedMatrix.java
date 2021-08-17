class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int row = matrix.length;
        int col = matrix.length;
        int startVal = matrix[0][0];
        int endVal = matrix[row-1][col-1];
        while(startVal <= endVal){
           int midVal = (startVal + endVal)/2;
            //ROW-WISE TRAVERSING THE MATRIX
            int result = 0;
            for(int i=0;i< row;i++){
                //APPLYING BINARY SEARCH ON EACH ROW
                int low = 0,high = (col -1),middle;
                while(low <= high){
                    middle = high + low /2;
                    if(matrix[i][middle] <= midVal){
                        low = middle +1 ;
                    }
                    else {
                        high =  middle - 1;
                    }
                  }
                result += low;
            }
            if(result < k){
                startVal = midVal + 1;
            }
            else {
                endVal = midVal - 1;
            }
        }   
        return startVal;
    }
}