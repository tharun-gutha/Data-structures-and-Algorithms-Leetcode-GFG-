class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=0
        last=len(nums)-1
        for i in range(len(nums)):
            mid=(first+last)//2
            if(target==nums[mid]):
                return mid
            elif target<nums[mid]:
                last=mid-1
            else:
                first=mid+1

        if(i==len(nums)-1):
            return -1

#Time complexity:O(N)
#Space complexity:O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=0
        last=len(nums)-1
        while first<=last:
            mid=(first+last)//2
            if(target==nums[mid]):
                return mid
            elif target<nums[mid]:
                last=mid-1
            else:
                first=mid+1
        return -1

#Time complexity:O(logN)
#Space complexity:O(1)
