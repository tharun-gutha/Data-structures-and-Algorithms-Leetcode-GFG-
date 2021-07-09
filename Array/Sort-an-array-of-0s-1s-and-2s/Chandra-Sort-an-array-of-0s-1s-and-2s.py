def sort012(arr):
    l=[]
    for i in arr:
        if i==0:
            l.append(i)
    for i in arr:
        if i==1:
            l.append(i)
    for i in arr:
        if i==2:
            l.append(i)
    i=0      
    while i<len(arr):
        arr[i]=l[i]
        i=i+1
        
# Time Complexity-O(n)

