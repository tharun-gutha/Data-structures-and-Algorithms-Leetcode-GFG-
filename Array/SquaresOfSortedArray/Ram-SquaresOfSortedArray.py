#First method- Take Time complexcity O(NLOGN) 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            n=i*i
            l.append(n)
        l.sort()
        return l


#Second Method - Take Time complexcity O(N)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)==0:
            return []
        
        ar=[0]*len(nums)
        l=0
        r=len(nums)-1
        loc=r
        
        while l<=r:
            ls=nums[l]*nums[l]
            rs=nums[r]*nums[r] 
            
            if ls<=rs:
                ar[loc]=rs
                r-=1
                loc-=1
            else:
                ar[loc]=ls
                l+=1
                loc-=1
        
        return ar