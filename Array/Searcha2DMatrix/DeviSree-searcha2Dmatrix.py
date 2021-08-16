class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len=len(matrix)
        col_len=len(matrix[0])
        for i in matrix:
            if i[col_len-1]>=target:
                for j in i:
                    if j==target:
                        return True
            else:
                pass
        return False   
#n + n
#time complexity -O(n)  

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len=len(matrix)
        col_len=len(matrix[0])
        for i in matrix:
            if i[col_len-1]>=target:
                l=0
                r=col_len-1
                while l<=r:
                    mid=(l+r)//2
                    if i[mid]==target:
                        return True
                    elif i[mid]>target:
                        r=mid-1
                    else:
                        l=mid+1
            else:
                pass
        return False  
# n+logn        
# time complexity -O(n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len=len(matrix)
        col_len=len(matrix[0])
        l=0
        r=row_len-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mid][-1]>=target and matrix[mid][0]<=target:
                left=0
                right=col_len-1
                while left<=right:
                    m=(left+right)//2
                    if matrix[mid][m]==target:
                        return True
                    elif matrix[mid][m]<target:
                        left=m+1
                    else:
                        right=m-1
                return False        
            elif matrix[mid][-1]<target:
                l=mid+1
            elif matrix[mid][0]>target:
                r=mid-1
        return False   
# logn + logn        
# time complexity - O(logn)        

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mid][-1]<target:
                l=mid+1
            elif matrix[mid][0]>target:
                r=mid-1
            else:
                break
        if not(l<=r):
            return False
        mid=(l+r)//2
        left=0
        right=len(matrix[0])-1
        while left<=right:
            m=(left+right)//2
            if matrix[mid][m]<target:
                left=m+1
            elif matrix[mid][m]>target:
                right=m-1
            else:
                return True
                
        return False        

        
#logn + logn            
#time complexity - O(logn)

