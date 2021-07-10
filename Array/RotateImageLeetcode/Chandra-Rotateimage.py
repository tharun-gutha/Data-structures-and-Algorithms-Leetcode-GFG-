
def rotate(matrix):
    le=len(matrix)
    i=0
    while i<le:
        k=(le)-1
        
        l=[]
        while k>=0:
            l.append(matrix[k][i])
            k=k-1
        matrix.append(l)
        i=i+1
    i=0
    j=le
    while i<le:
        matrix[i]=matrix[j]
        matrix[j]=None
        
        i,j=i+1,j+1
    i=0
    while i<le:
        matrix.pop()
        i=i+1
# Time Complexity-O(n**2)
# Space Complexity-O(n**2)