'''
class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
'''
class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            search=target-nums[i]
            if (search in nums[i+1:]):
                j=nums.index(search)
                if(search==nums[i]):
                     j=nums.index(search,i+1)
                return [i,j]


li=[3,3]
s=Solution()
res=s.twoSum(li,6)
print(res)

 

            
                
                


 

            
                
                