class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        def countLessEqual(num):
            count=0
            for row in matrix:
                left=0
                right=n
                while left<right:
                    mid=(left+right)//2
                    if row[mid]<=num:
                        left=mid+1
                    else:
                        right=mid
                count+=left
            return count
        left=matrix[0][0]
        right=matrix[-1][-1]
        while left<right:
            mid=(left+right)//2
            if countLessEqual(mid)<k:
                left=mid+1
            else:
                right=mid
        return left        
                
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        def countLessEqual(num):
            count=0
            for row in matrix:
                left=0
                right=n
                while left<right:
                    mid=(left+right)//2
                    if row[mid]<=num:
                        left=mid+1
                    else:
                        right=mid
                count+=left
            return count
        left=matrix[0][0]
        right=matrix[-1][-1]
        while left<right:
            mid=(left+right)//2
            if countLessEqual(mid)<k:
                left=mid+1
            else:
                right=mid
        return left        
                
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        def countLessEqual(num):
            count=0
            for row in matrix:
                for i in row:
                    if i<=num:
                        count+=1
            return count
        left=matrix[0][0]
        right=matrix[-1][-1]
        while left<right:
            mid=(left+right)//2
            if countLessEqual(mid)<k:
                left=mid+1
            else:
                right=mid
        return left        
                
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
       res=[]
       for s in matrix:
            res+=s
       res.sort()
       return res[k-1]
        
                
                                