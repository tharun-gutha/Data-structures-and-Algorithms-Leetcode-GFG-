class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))                # to eliminate duplicates       - o(n)
        nums.sort()                         # o(nlogn)
        count =0
        c=[]
        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):        
            if nums[i+1]-nums[i]==1:   # if consecutive increment count
                count+=1
            else:
                if count>0:                 
                    count+=1     
                c.append(count)            # append the count   
                count=0                                  
        count+=1                           
        c.append(count)                    # append the count so as to cover the last consecutive sequence length
        return max(c)                      # return the length of max 

# time complexity - o(nlogn) and takes extra space 



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        tempcount=0
        maxcount=0
        for i in range(len(nums)):
            tempcount+=1
            print(tempcount)
            if i==0: continue
            elif nums[i]-nums[i-1]==0: tempcount-=1
            elif nums[i]-nums[i-1]!=1: tempcount=1
            elif nums[i]-nums[i-1]==1: maxcount=max(tempcount,maxcount)
        return max(maxcount,tempcount)    
# time complexity -o(nlogn) but less extra space 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        longest=0
        for i in nums:
            if i-1 not in nums_set: #checking if the element i is the start of the sequence 
                length=0
                while (i+length) in nums_set: # then continuing to find the next consecutive elements and increasing the length 
                    length+=1
                longest=max(length,longest)  
        return longest        
        
# time complexity -o(n)         
       



