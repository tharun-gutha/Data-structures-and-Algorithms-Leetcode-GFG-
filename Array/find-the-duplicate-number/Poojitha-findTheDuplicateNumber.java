Method 1:- complextity - O(nlogn)
class Solution {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == nums[i+1])
                return nums[i];
      }
        return -1;
    }
}
method 2 :- complextity-O(n)
class Solution {
    public int findDuplicate(int[] nums) { 
        int low =0,high=nums.length-1;
        int duplicate = -1;
        while(low <= high){
            int mid = low + (high - low)/2;
            
            int count =0;
            for(int num : nums){
                if(num <= mid){
                    count ++;
                }
            }
            if(count > mid){
                duplicate = mid;
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return duplicate;
     }
}