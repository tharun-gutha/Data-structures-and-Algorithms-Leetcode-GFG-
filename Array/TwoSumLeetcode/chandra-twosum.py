def twosum(nums,target):
    if (len(nums)>=2 and len(nums)<=10000) and (target>=(-10**9) and target<=(10**9)):
        i=0
        while i<len(nums)-1:
            if not((nums[i]>=pow(-10,9)) and (nums[i]<=(10**9))) or not((nums[i+1]>=(-10**9)) and (nums[i+1]<=(10**9))):
         
                return []
            i=i+1    
        i=0        
        while i<len(nums):
            j=0
            while j<len(nums):
                if i==j:
                    j=j+1
                    continue
                if nums[i]+nums[j]==target:
                    return [i,j]
                j=j+1
            i=i+1
    else:
        return []
print(twosum([1,2,3,3],6))                
# Time Complexity is O(n**2)
# Space Complexity is O(n)
            
            
            



