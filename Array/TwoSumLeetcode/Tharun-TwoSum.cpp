class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> result;
        map<int,int> m;
        for(int i=0;i<nums.size();i++)
        {
            if(m.find(target-nums[i])!=m.end())
            {
                result.push_back(m[target-nums[i]]);
                result.push_back(i);
                return result;
            }
            else
            {
                m[nums[i]]=i;
            }
        
        }
        return result;
    }
};