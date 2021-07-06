'''
# finding the missing element on searching
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=len(nums) #size of the list
        m=max(nums) #maximum element of the list
        nums.sort() #sort the list
        if(s==m+1): 
            return m+1
        else:
            for i,j in zip(range(m),nums):
                if(i!=j):
                    return i
'''
#finding the missing element based on difference from actual sum of numbers 
 class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        actualsum=int(n*(n+1)/2)
        listsum=sum(nums)
        diff=actualsum-listsum
        if(0 not in nums):
            return 0
        return diff

li=[1,2]
s=Solution()
res=s.missingNumber(li)
print(res)


 

            
                
                
               


                    
        