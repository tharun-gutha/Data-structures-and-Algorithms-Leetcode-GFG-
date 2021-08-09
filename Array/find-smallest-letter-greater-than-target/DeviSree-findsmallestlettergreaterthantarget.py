class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i>target:
                return i
        return letters[0]    
# time complexity - o(n)

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low=0
        high=len(letters)-1
        while low<=high:
            mid=(low+high)//2
            if target>=letters[mid]:
                low=mid+1
            elif target<letters[mid]:
                high=mid-1
            if letters[mid]>target and not letters[mid-1]>target:
                return letters[mid]
                
        return letters[0]        
# time complexity -o(nlogn) 

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low=0
        high=len(letters)-1
        result=letters[0]
        while low<=high:
            mid=(low+high)//2
            if target>=letters[mid]:
                low=mid+1
            else:
                result=letters[mid]
                high=mid-1        
        return result        
#time complexity - o(nlogn)               
                
                       
                
                     
        