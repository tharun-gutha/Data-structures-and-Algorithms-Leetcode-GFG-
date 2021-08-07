class Solution:
    def search(nums,target):
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                h=mid-1
            elif target>nums[mid]:
                l=mid+1
        return -1
# Time Complexity-O(logn)