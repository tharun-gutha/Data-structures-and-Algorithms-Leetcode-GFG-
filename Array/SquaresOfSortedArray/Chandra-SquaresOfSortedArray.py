 def sortedSquares(nums):
        list=[]
        for i in nums:
            list.append(i**2)
    
        list.sort()
        return list
# Time Complexity -O(nlogn)
#--------------------------------------------------------------
import math
def sortedSquares(nums):
        l=[]
        for i in nums:
            l.append(0)
        i,j,k=0,len(nums)-1,1
        while i!=j:
            if math.fabs(nums[i])>=math.fabs(nums[j]):
                l[-k]=nums[i]**2
                k=k+1
                i=i+1
            else:
                l[-k]=nums[j]**2
                k=k+1
                j=j-1
        l[-k]=nums[i]**2
        return l
#Time Complexity-O(n)
           