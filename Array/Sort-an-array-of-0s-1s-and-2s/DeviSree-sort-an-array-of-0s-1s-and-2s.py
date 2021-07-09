
class Solution:
    def sort012(self,arr,n):
        '''
        # first method - o(n^2)
        res=[]
        for i in arr:
            for j in arr:
                if i<=j:
                    res.append(i)
        return res
        '''
        #second method - o(nlogn)
        #arr.sort()

        #third method - o(n)
        a=[]
        b=[]
        c=[]
        for i in arr:            
            if i==0:
                a.append(i)
            elif i==1:
                b.append(i)
            elif i==2:
                c.append(i)
        
        return a+b+c
s=Solution()
res=s.sort012([0,2,1,2,0],5)
print(res)

