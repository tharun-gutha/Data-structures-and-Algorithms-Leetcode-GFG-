def containsDuplicate(nums):
        dict={}
        for i in nums:
            if i in dict:
                dict[i]=dict[i]+1
            if i not in dict:
                dict[i]=1
        for i in dict:
            if dict[i]>=2:
                return True
        return False
#Time Complexity-O(n**2)
#------------------------------------------------------
def containsDuplicate(nums):
        if len(set(nums))!=len(nums):
            return True
        else:
            return False
# Time Complexity-O(n)

        