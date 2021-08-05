class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        contains_one=False
        for i in nums:
            if i==1:              // checking if the list contains 1 or not 
                contains_one=True
                break 
                
        if not contains_one:  // if it doesnot contain 1 then return 1 
            return 1
        
        n=len(nums)
        
        if n==1:              // if size of the list is 1 , then the value is 1 so return 2 
            return 2
        
        for i in range(n):
            if ( nums[i]<=0 or nums[i]>n) :   // if elements are greater than the length replace it with value 1 
                nums[i]=1
                
        for i in range(n):                   // now checking if a absolute value of the number exists, if it exists then change the value at its index, from positive to negative 
            x = abs(nums[i])                 //example:  [1,3,1]
            if nums[x-1]>0:                  //          [-1,1,-1] => so position 2(index 1) has positive ,so element to return is 2 
                nums[x-1]*=-1
                
        for i in range(n):
            if nums[i]>0:
                return i+1 
            
        return n+1    
    
    
    