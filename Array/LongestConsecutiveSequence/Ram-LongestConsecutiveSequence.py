class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new=set(nums)
        res=0
        for i in new:
            if i-1 not in new:
                start=i
                while start in new:
                    start+=1
                res=max(res,start-i)
        return res
        
#time complexcity=O(n)