// the main idea is storing elements in map return true if element is already there else return false
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n=nums.size();
        map<int,int> m;
        for(int i=0;i<n;i++){
            if(m.find(nums[i])!=m.end())
            {
                return true;
            }
            else
            {
                m[nums[i]]=i;
            }
        }
        return false;
    }
};