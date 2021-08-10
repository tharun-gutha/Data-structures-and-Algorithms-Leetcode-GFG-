
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for key in d:
            if d[key]>=2:
                return key
# time-complexity - o(n)