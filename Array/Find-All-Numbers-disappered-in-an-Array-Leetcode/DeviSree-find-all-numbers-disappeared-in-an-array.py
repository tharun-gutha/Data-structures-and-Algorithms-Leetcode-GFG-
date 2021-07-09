#first method - looping through range and checking with nums elements
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)      
        return res        
                
# first method - exceed the time limit 

# second method - converting into sets and performing difference operation

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(1,len(nums)+1):
            res.append(i)
        set1=set(res)    
        set2=set(nums)
        diff=set1-set2
        return diff    

#third method - o(n)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing=[]#create a missing value
        for i in nums:
            pos=abs(i)-1  # we get to the position (ie index ) 
            if nums[pos]>0:
                nums[pos]*=-1 # turn the element into negative element (as marked )
        for i in range(len(nums)):
            if nums[i]>0:
                missing.append(i+1) #getting back to position from index (these are elements )
        return missing        
                
        