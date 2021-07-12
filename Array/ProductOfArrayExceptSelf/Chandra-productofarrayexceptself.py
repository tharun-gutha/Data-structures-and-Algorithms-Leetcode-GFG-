def productExceptSelf(nums):
        l=[]
        i=0
        while i<len(nums):
            j=0
            product=1
            while j<len(nums):
                if i==j:
                    j=j+1
                    continue
                product*=nums[j]
                j=j+1
            l.append(product)
            i=i+1
        return l
#Time Complexity-O(n**2)
#----------------------------------------------------------
def productExceptSelf(nums):
        l=[x for x in range(len(nums))]
        l[0]=1
        i=1
        while i<len(nums):
            l[i]=nums[i-1]*l[i-1]
            i=i+1
        i=len(nums)-1
        right=1
        while i>=0:
            l[i]=l[i]*right
            right=nums[i]*right
            i=i-1
        return l
# Time Complexity-O(n)
                