from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        obj = dict()
        for i in nums:
            if i in obj:
                obj[i]=False
            else:
                obj[i]=True
        for key,value in obj.items():
            if value==True:
                return key
        