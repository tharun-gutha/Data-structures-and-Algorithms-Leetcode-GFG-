
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            arr.append(pow(i,2))
        return sorted(arr)