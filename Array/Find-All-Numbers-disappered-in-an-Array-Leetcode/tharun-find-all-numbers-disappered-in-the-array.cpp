// the main idea is first we go through the array take one element, and we mark negative at element value index-1 

//example [4,3,2,7,8,2,3,1] take 4 as element we go to index 3(element-1) and mark it as negative value.repeat for every element and finally we get some postive values those are the missing numbers.


class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> v; //vector to store the result
        int n=nums.size(); // size of the vector
        for(int i=0;i<n;i++)
        {
            int temp=nums[i];
            temp=(temp>0)?temp:-temp;
            if(nums[temp-1]>0)
            {
                nums[temp-1]*=-1;
            }
        }
        for(int i=0;i<n;i++)
        {
            if(nums[i]>0)
            {
                v.push_back(i+1);
            }
        }
        return v;
    }
};

//time complexity O(n);
