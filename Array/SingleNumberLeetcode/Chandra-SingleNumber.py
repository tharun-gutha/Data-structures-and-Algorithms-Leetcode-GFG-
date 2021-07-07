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
