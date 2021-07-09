def findDisappearedNumbers(nums):
        s1={x for x in range(1,len(nums)+1)}
        s2=set(nums)
        return s1-s2
# Time Complexity-O(n)
# But Extra Space Is Used
#---------------------------------------------------------------------
def findDisappearedNumbers(nums):
        l=[]
        for i in nums:
            pos=abs(i)-1
            if nums[pos]>0:
                nums[pos]=nums[pos]*-1
            
        for i in range(len(nums)):
            if nums[i]>0:
                l.append(i+1)
        return l
# Time Complexity-O(n)
# Extra Space Is Not Used
        