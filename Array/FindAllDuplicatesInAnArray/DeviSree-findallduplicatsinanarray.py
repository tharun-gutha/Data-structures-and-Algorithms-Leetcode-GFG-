# first method
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        B=list(set(nums))
        for i in B :
            nums.remove(i)
        return nums    
# time complexity - o(n^2)
# time exceeds 

# second method
    class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #the values are in the range [1,n]
        output=[] # creating a empty list
        for i in nums: # traverse every element
            j=abs(i) # find absolute value of it
            if nums[j-1]<0: # if elements at the position is negative then add it output
                output.append(j)
            else:
                nums[j-1]*=-1 # else change element at the position into negative element
        return output 

        #time complexity - o(n)
        
        '''
        example demonstration : (for clear understanding )

        [4,3,2,7,8,2,3,1]
        for j (4)
        [4,3,2,-7,8,2,3,1]
        for j  (3)
        [4,3,-2,-7,8,2,3,1]
        for j (2)
        [4,-3,-2,-7,8,2,3,1]
        for j (7)
        [4,-3,-2,-7,8,2,-3,1]
        for j (8)
        [4,-3,-2,-7,8,2,-3,-1]
        for j (2)
        [4,-3] # at position 2 we find negative value saying that 2 already exists
        so output.append(2)---> output=[2]
        for j (3)
        [4,-3,-2] # at position 3 we find negative value saying that 3 already exists
        so output.append(3)----> output=[2,3]
        for j (1)
        [-4,-3,-2,-7,8,2,-3,-1]

        output=[2,3]
    
        '''

        
             