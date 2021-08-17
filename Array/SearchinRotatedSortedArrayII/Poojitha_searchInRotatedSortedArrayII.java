Method 1:- complextity - O(n logn)
class Solution {
    public boolean search(int[] nums, int target) {
      if(nums.length == 0){
          return false;
      }  
      for(int i = 0;i < (nums.length-1);i++){
          if(target == nums[i]){
              return true;
          }
      }  
     return false;
    }
}
Method 2:-complexity - O(logn)
class Solution {
    public boolean search(int[] nums,int target) {
          int start = 0,end = (nums.length-1);
          while(start <= end){
              int mid = start + (end - start)/2;
              if(nums[mid] == target){
                  return true;
              }
              //LEFT HALF IS SORTED
              if(nums[start] < nums[mid]){
                  if(target >= nums[start] && target <= nums[mid]){
                      end = mid - 1;
                  }
                  else{
                      start = mid +1 ;
                  }
              }
              //RIGHT HALF IS SORTED
              else if(nums[mid] < nums[start]){
                  if(target > nums[mid] && target < nums[start]){
                      start = mid + 1;
                  }
                  else{
                      end = mid - 1;
                  }
              }
              else {
                  /* WHEN WE ARE NOT SURE ON WHICH HALF THE VALUE PRESENT ,
                  i.e....., NUMS[START] == NUMS[MID] == NUMS[END]
                  start++;*/
              }
          }
        return false;
    }
}    