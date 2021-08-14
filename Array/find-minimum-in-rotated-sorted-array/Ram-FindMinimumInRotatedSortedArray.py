class Solution:
    def findMin(self, nums: List[int]) -> int:
        first,last= 1,len(nums)-1
        
        while first<=last:
            mid=first+(last-first)//2
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid]<nums[0]:
                last= mid
            else:
                first= mid+1
                
        return nums[0]
        
#Time Complexcity=O(logN)