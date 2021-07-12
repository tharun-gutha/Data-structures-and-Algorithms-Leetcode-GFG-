
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[1]*len(nums)
        prfx=1
        for i in range(len(nums)):
            p[i]=prfx #storing prefix product of each element of nums array into resultant array
            prfx*=nums[i]
        post=1
        for i in range(len(nums)-1,-1,-1):
            p[i]*=post #multiplying postfix product of each element of nums array with prefix product and storing required o/p values in resultant array 
            post*=nums[i]
        return p
        