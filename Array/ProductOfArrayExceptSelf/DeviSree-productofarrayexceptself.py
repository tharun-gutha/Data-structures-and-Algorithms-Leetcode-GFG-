class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # right list - it contains product of elements to the right of each element 
        output=[1]
        for i in range(len(nums)-1,0,-1):
            output.append(output[-1]*nums[i])
        output=output[::-1]# reverse the list
        # left list - it adds the product of elements to the left of a particular element to the output list elements 
        left=1
        for i in range(len(nums)):
            output[i]*=left
            left*=nums[i]
        return output    