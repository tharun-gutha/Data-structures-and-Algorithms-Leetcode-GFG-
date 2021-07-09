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
    return l
# Time Complexity-O(n)

