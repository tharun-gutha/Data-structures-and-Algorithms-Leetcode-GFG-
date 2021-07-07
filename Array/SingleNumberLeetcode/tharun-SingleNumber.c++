class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n=nums.size();//storing size of the array
        int x=nums[0];//assign first element to x varaible 
        for(int i=1;i<n;i++){
            x=x^nums[i]; // the main idea is for checking single number and this kind of quesions like  missing number go for XOR bit wise operator 
            //you can implement by using map but it takes extra space.
        }
        return x;
    }
};