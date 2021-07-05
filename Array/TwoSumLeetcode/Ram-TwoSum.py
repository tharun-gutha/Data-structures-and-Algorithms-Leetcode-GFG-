nums=[2,7,11,15]
target=9
def twosum(nums,target):
    d={}
    for i in range(len(nums)):
        y=target-nums[i]
        if y in d.keys():
            return[d[y],i] 
        else:
            d[nums[i]]=i #push array values as keys and array indices as values into the dictonary 
    return[]

print(twosum(nums,target))
