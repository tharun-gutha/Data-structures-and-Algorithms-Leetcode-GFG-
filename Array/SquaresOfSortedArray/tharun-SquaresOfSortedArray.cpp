class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> v;
        int n=nums.size();
        if(n==1)
        {
            nums[0]=nums[0]*nums[0];
            return nums;
        }
        int i=0,j=n-1;
        while(i<j)
        {
            if(nums[i]<0)
            {
                nums[i]=-nums[i];
            }
            if(nums[i]>nums[j])
            {
                v.push_back(nums[i]*nums[i]);
                i++;
            }
            else if(nums[i]<nums[j]){
                v.push_back(nums[j]*nums[j]);
                j--;
            }
            else if(nums[i]==nums[j])
            {
                v.push_back(nums[i]*nums[i]);
                v.push_back(nums[i]*nums[i]);
                i++;
                j--;
            }
        }
        if(j==i)
        {
            v.push_back(nums[i]*nums[i]);
        }
        
        reverse(v.begin(),v.end());
        return v;
    }
};