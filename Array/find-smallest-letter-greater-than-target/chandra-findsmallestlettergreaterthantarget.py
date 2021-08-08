class Solution:
    def nextGreatestLetter(letters,target):
        l=len(letters)
        i=0
        while i<l:
            if letters[i]>target:
                return letters[i]
            i=i+1
        return letters[0]
#Time complexity-O(n)
#--------------------------------------------------------------
class Solution:
    def nextGreatestLetter(letters,target):
        l=0
        h=len(letters)-1
        result=letters[0]
        while l<=h:
            mid=(l+h)//2
            if letters[mid]==target:
                l=mid+1
            elif letters[mid]<target:
                l=mid+1
            else:
                result=letters[mid]
                h=mid-1
        return result
#Time complexity-O(logn)