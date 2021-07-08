class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # checking if the list of elements are already strictly increasing 
        for i in range(len(nums)):
              if(i==len(nums)-1):
                return True
              if(nums[i]<nums[i+1]):
                pass  
              else:
                    break
        # checking if the list of elements after removing any one would be strictly increasing #or not         
        for i in range(len(nums)):
            temp=nums.copy()
            temp.pop(i)
            
            for j in range(len(temp)):
                if(j==len(temp)-1):
                    return True
            
                if temp[j]<temp[j+1]:
                    pass
                else:
                    break
             
        return False     
            
     
        