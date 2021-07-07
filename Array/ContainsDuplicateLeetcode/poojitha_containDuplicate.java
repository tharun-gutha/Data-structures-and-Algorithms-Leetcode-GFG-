class Solution {
    public boolean containsDuplicate(int[] nums) {
        //METHOD 1:-
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<i;j++){
               if(nums[i] == nums[j]){
                  return true;
                }
               else{
                  return false;
               } 
            }
        }
        return false;
    //METHOD 2:-
       Arrays.sort(nums);
         for (int i = 0; i < nums.length - 1; ++i) {
           if (nums[i] == nums[i + 1]){
            return true;
            } 
         }  
         return false;     
    }
}