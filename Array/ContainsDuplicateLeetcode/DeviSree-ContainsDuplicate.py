#first method - taking a dictionary to store count of elements
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}# take an empty dictionary
        for i in nums:
            if i not in d:
                d[i]=1# if element is not in d intialize its count as 1 by inserting it
            else:
                d[i]+=1# if element is present then increment its count (duplicate )
            
        for j in d.values():
            if j>1:
                return True
        return False    

#second method - converting list into set and finding the length        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # calculating the length of set from the list and finding the actual list length
        actual=len(nums)
        asset=len(set(nums))
        # set doesnt allow duplicates . so, if duplicates are presenet then lengths are not same
        if(actual!=asset):
            return True
        else:
            return False