def findDuplicates(nums):
        d={}
        l=[]
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            if i not in d:
                d[i]=1
        print(d)
        for i in d:
            if d[i]==2:
                l.append(i)
        return l
# Time Complexity-O(n**2)
# It Will Take Extra space
#----------------------------------------------------
from math import *
def findDuplicates(nums):
    i=0
    l=[]
    while i<len(nums):
        ele=floor(fabs(nums[i]))
        x=ele-1
        
        if nums[x]<0:
            l.append(ele)
        else:
            nums[x]=nums[x]*-1
        i=i+1
    return l
#Time Complexity-O(n)