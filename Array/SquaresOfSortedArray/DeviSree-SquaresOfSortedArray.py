# first method - using a built in sort function
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq=[] # creating new list
        for i in nums:
            sq.append(i*i) # adding each element of nums after squaring 
        sq.sort() # sort the list sq 
        return sq

# second method - sorting while squaring the elements   
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        k=len(nums)-1
        s=[]
        for p in range(len(nums)):
            s.append(0)
        while i!=j:
            if nums[i]*nums[i]>nums[j]*nums[j]:
                s[k]=nums[i]*nums[i]
                i+=1
            else:
                s[k]=nums[j]*nums[j]
                j-=1
            k-=1
        s[k]=nums[i]*nums[i]
        return s    
               