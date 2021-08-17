Method 1 :- complexity-O(n^2)
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix.length == 0){
            return false;
        }
        int rows = matrix.length-1;
        int cols = matrix.length-1;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(matrix[i][j] == target){
                    return true;
                }
            }
        }
        return false;
    }
}
Method 2:-complexity-O(log n) using binary search
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix.length == 0){
            return false;
        }
        int rows = matrix.length;
        int cols = matrix.length;
        int first = 0,last = rows * cols - 1;
        while(first <= last){
            int mid = first + (last - first)/2;
            //[mid/col]-- gets row & [mid%cols]--gets column
            int mid_element = matrix[mid / cols][mid % cols];
            if(mid_element == target){
                return true;
            }
            else if(target < mid_element){
                last = mid - 1;
            }
            else {
                first = mid + 1;
            }
        }
       return false;
    }
}