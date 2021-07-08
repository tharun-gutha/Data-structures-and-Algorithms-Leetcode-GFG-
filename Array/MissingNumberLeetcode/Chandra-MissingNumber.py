def missingnumber(nums):
    n=len(nums)
    sum1=n*(n+1)//2
    sum2=sum(nums)
    return sum1-sum2
#Time complexity -O(n)
#---------------------------------------------------
def missingNumber(nums): 
    a=0
    for i in range(len(nums)+1):
        a=a^i
    for i in nums:
        a=a^i
    return a
#Time Complexity-O(n)    
        