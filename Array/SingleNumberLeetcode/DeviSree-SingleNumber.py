#first method - sorting the elements and finding the pairs , so unpaired results in single element
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums),2):
            if(i+1<len(nums) and nums[i]==nums[i+1]):
                pass
            else:
                return nums[i]
                
#second method - XoR function based , resulting in unpaired element              
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res^=i
        return res    
                
              