class Solution {
    public int missingNumber(int[] nums) {
        //METHOD 1:-
       /* int totalSum=nums.length*(nums.length + 1)/2;
        int actualSum=0;
        for(int i=0;i<nums.length;i++){
            actualSum += nums[i];
        }
        return totalSum - actualSum;*/
        //METHOD 2:-
        int missing_num=nums.length;
        for(int i=0;i<nums.length;i++){
           missing_num ^= i ^ nums[i];
        }
        return missing_num;
        
    }
}