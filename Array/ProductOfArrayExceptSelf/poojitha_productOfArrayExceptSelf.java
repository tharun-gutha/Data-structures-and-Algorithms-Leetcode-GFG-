method-1:-complexity-O(n^2)
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] arr=new int[nums.length];
        for(int i=0;i<nums.length;i++){
           int mul=1;
            for(int j=0;j<nums.length;j++){
                if(i==j){
                    continue;
                }
                mul *= nums[j]; 
            }
            arr[i]=mul;
        }
         return arr;
    }
}
method-2:-complexity-O(n)
import java.lang.*;
class Solution {
public int[] productExceptSelf(int[] nums) {
    int mul = 1;
    for(int i = 0; i < nums.length; i++) {
        mul *= nums[i];
    }
    
    for (int i = 0; i < nums.length; i++) {
        nums[i] = mul / nums[i];
    }
    return nums;
 }
} 
    