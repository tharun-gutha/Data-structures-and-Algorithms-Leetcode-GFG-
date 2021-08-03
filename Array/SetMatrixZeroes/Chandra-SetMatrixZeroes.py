def setZeroes(matrix):
        m=len(matrix)
        n=len(matrix[0])
        i=0
        while i<m:
            j=0
            while j<n:
                if matrix[i][j]==0:
                    k=0
                    while k<n:
                        if matrix[i][k]!=0:
                            matrix[i][k]='x'
                        k=k+1
                    l=0
                    while l<m:
                        if matrix[l][j]!=0:
                            matrix[l][j]='x'
                        l=l+1
                    
                j=j+1
            i=i+1
        i=0
        while i<m:
            j=0
            while j<n:
                if matrix[i][j]=='x':
                    matrix[i][j]=0
                j=j+1
            i=i+1
#Time Complexity-O(n**3)
# It Uses Constant space
#----------------------------------------------------------------------------
def setZeroes(matrix):
        m=len(matrix)
        n=len(matrix[0])
        l1=[]
        l2=[]
        for i in range(m):
            l1.append(1)
        for i in range(n):
            l2.append(1)
        print(l1)
        print(l2)
        i=0
        while i<m:
            j=0
            while j<n:
                if matrix[i][j]==0:
                    l1[i]=0
                    l2[j]=0
                j=j+1
            i=i+1
        i=0
        while i<m:
            j=0
            while j<n:
                if l1[i]==0 or l2[j]==0:
                    matrix[i][j]=0
                j=j+1
            i=i+1
#Time Complexity-O(n**2)
# But It Takes Extra Space