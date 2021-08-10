class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        r={}
        for i in nums:
            if i not in r:
                r[i]=1
            else:
                r[i]+=1
        for k in nums:
            if r[k]>=2:
                return k
    
#Time Complexcity=O(N)