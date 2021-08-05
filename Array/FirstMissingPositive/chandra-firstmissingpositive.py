class Solution:
    def firstMissingPositive(nums):
        i,j=0,len(nums)
        while i<j:
            
            if nums[i]<=0 or nums[i]>=j or nums[i]==i+1:
                i=i+1
                continue
            
            if nums[i]>0 and nums[i]<j:
                temp=nums[i]
                nums[i]=nums[temp-1]
                if nums[i]==temp:
                    i=i+1
                    continue
                nums[temp-1]=temp
        
               
            
          
        i=0
        while i<j:
            if nums[i]==i+1:
                i=i+1
            else:
                return i+1
        return i+1
# time complexity -O(n)
# space complexity -O(1) didnt take extra space