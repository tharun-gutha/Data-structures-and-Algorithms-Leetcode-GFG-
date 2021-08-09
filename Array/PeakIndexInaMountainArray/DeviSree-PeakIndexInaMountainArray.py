class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                pass
            else:
                return i
# time complexity - o(n)   
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid-1]:
                low=mid+1
            else:
                high=mid-1
        return mid        
# time complexity - o(nlogn)                 