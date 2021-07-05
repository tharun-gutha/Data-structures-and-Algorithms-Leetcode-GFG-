

def twosum(nums,target):
     if (len(nums)>=2 and len(nums)<=10000) and (target>=(-10**9) and target<=(10**9)):
            i=0
            while i<len(nums)-1:
                if not((nums[i]>=pow(-10,9)) and (nums[i]<=(10**9))) or not((nums[i+1]>=(-10**9)) and (nums[i+1]<=(10**9))):
         
                    return []
                i=i+1    
            i=0
            j=0
            while j<len(nums):
                
                
                while i<len(nums):
                    if i==j:
                        i=i+1
                        continue
                
                    if (nums[i]+nums[j])==target:
                        return [i,j]
                    i=i+1
                i=0    
                j=j+1
     else:
        return []        
    


