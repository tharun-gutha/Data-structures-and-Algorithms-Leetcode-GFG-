class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            if nums[i]>0 and nums[i]-1<len(nums) and nums[i]!= nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i+=1
                
        for i, integer in enumerate(nums):
            if integer!=i+1:
                return i+1
        return len(nums)+1
#time complexcity=O(n)
#space complexcity=O(1)



class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        len1 = len(nums)
        if len1 == 0:
            return 1
        dic = {}
        for num in nums:
            if num > 0:
                dic[num] = num
        for i in range(1, len1 + 1):
            if dic.get(i, -1) == -1:
                return i
        return len1 + 1      
#here the dictionary will use 0 (n) space
#time complexcity=O(n)
