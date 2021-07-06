class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n=nums.size();
        int totalSum=(n*n+n)/(2);
        int arraySum=0;
        for(int i=0;i<nums.size();i++)
        {
            arraySum=arraySum+nums[i];
        }
        return totalSum-arraySum;
    }
};

// to avoid overflow we solve using XOR operator
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n=nums.size();
        int x1=nums[0],x2=0;
        for(int i=1;i<n;i++){
            x1=x1^nums[i];
        }
        for(int j=1;j<=n;j++){
            x2=x2^j;
        }
        return (x1^x2);
    }
};