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
        