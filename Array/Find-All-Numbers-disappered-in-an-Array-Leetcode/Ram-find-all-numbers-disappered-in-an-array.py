class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            loc=abs(i)-1
            if nums[loc]>0:
                nums[loc]*=-1
        
        for i in range(len(nums)):
            if nums[i]>0:
                l.append(i+1)
        
        return l
        