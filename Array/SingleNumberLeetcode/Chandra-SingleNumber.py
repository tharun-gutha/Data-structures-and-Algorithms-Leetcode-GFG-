 def singleNumber(nums):
        dict={}
        for i in nums:
            if i in dict:
                dict[i]=dict[i]+1
            if i not in dict:
                dict[i]=1
            
        for i in dict:
            if dict[i]==1:
                return i
#Time Complexity-O(n**2)
#-------------------------------------------------
def singleNumber(nums):
        return 2*(sum(set(nums)))-sum(nums)
#Time Complexity -O(n)
#-----------------------------------------------------
def singleNumber(nums):
        x=0
        for i in nums:
            x=x^i
        return x
        
