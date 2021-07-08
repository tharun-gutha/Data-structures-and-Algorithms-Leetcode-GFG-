
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            arr.append(pow(i,2))
        return sorted(arr)


#Another method
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        left = 0
        right = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            leftAbs = nums[left] **2
            rightAbs = nums[right]**2
            if leftAbs>=rightAbs:
                arr[i]=leftAbs
                left+=1
            else:
                arr[i]=rightAbs
                right-=1
                
        return arr
            
        