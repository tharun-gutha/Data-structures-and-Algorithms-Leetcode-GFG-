class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(0,len(arr)):
            if(arr[i]>arr[i+1]):
                break
        return i