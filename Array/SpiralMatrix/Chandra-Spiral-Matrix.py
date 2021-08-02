def spiralOrder(matrix):
        t,l=0,0
        b=len(matrix)-1
        r=len(matrix[0])-1
        dir=0
        lis=[]
        while (l<=r and t<=b):
            if dir==0:
                i=l
                while i<=r:
                    lis.append(matrix[t][i])
                    i=i+1
                t=t+1
            elif dir==1:
                i=t
                while i<=b:
                    lis.append(matrix[i][r])
                    i=i+1
                r=r-1
            elif dir==2:
                i=r
                while i>=l:
                    lis.append(matrix[b][i])
                    i=i-1
                b=b-1
            elif dir==3:
                i=b
                while i>=t:
                    lis.append(matrix[i][l])
                    i=i-1
                l=l+1
            dir=(dir+1)%4
        return lis
# Time Complexity-O(n**2)
   