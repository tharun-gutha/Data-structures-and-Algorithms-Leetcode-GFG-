Method 1:-complexity -O(n logn)
class Solution {
    public int findMin(int[] nums) {
        Arrays.sort(nums);
        for(int i=1;i<(nums.length);i++){
            if(nums[i]>nums[i-1]){
                return nums[i-1];
            }
        }
        return -1;
    }
}
Method 2:-complexity-O(log n)
class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];

        int left = 0;
        int right = n - 1;
    
        while (left < right) {
           int mid = left + (right - left) / 2;
           if (nums[mid] >= nums[left] && nums[mid] > nums[right]) {
               left = mid + 1;
           }
           else {
             right = mid;
           } 
        }
        return nums[left];  
    }
}    