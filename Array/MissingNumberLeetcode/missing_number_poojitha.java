class Solution {
    public int missingNumber(int[] nums) {
        
        int totalSum=nums.length*(nums.length + 1)/2;
        int actualSum=0;
        for(int i=0;i<nums.length;i++){
            actualSum += nums[i];
        }
        return totalSum - actualSum;
    }
}