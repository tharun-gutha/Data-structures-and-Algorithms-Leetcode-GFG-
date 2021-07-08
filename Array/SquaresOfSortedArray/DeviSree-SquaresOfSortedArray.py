class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq=[] # creating new list
        for i in nums:
            sq.append(i*i) # adding each element of nums after squaring 
        sq.sort() # sort the list sq 
        return sq
        