class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s=set()
        r=[]
        for i in nums:
            if(i in s):
                r.append(i)
            else:
                s.add(i)
        return r
        