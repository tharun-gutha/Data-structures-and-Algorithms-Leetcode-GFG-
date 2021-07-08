//import java.lang.Math;
class Solution {
    public int[] sortedSquares(int[] nums) {
       METHOD 1:-Timecomplexity(Ologn)
        Arrays.sort(nums);
        for(int i=0;i<nums.length;i++){
            nums[i]= nums[i]*nums[i];
        }
       Arrays.sort(nums);
        return nums;
        METHOD 2:-   
        int i=0;
        int j=nums.length-1;
        int[] result = new int[nums.length];
        int count = nums.length - 1;
        while(count >= 0) {
         if(Math.abs(nums[i]) > Math.abs(nums[j])) {
            result[count] = nums[i] * nums[i];
            i++;
          }
         else {
            result[count] = nums[j]*nums[j];
            j--;
          }
         count--;
        }
    return result;
    }
}