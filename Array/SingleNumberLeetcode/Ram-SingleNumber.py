#First Method - By storing list values into another list and By elemenating duplicate elements
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
            else:
                l.remove(i)
        return l[0]

 
        
#Second Method - By using XOR operator
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            n ^=i
        return n
