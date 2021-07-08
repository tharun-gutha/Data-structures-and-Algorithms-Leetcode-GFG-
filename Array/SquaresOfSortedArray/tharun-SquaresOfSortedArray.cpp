// time complexity o(n) and space o(n)
// use two pointer pattern to solve the problem and before submitting anaylyze some test cases where you solutin may go wrong
//
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> v(nums.size());
        int n=nums.size();//size of array
        if(n==1)//converting negative to postive numbers
        {
            nums[0]=nums[0]*nums[0];
            return nums;
        }
        int i=0,j=n-1,k=n-1;//taking two pointers and based on condition insert elements from back to front in the array
        while(i<j)
        {
            if(nums[i]<0)
            {
                nums[i]=-nums[i];
            }
            if(nums[i]>nums[j])
            {
                v[k]=(nums[i]*nums[i]);
                i++;
                k--;
            }
            else if(nums[i]<nums[j]){
                v[k]=(nums[j]*nums[j]);
                j--;
                k--;
            }
            else if(nums[i]==nums[j])
            {
                v[k]=(nums[i]*nums[i]);
                 k--;
                v[k]=(nums[i]*nums[i]);
                i++;
                j--;
                k--;
            }
        }
        if(j==i)
        {
            v[k]=(nums[i]*nums[i]);
        }
        return v;
    }
};