# nums=[3,0,1]
# def missingNumber(nums):
#     for i in range(len(nums)+1):
#         if i in nums:
#             pass
#         else:
#             return i

# print(missingNumber(nums))



# nums=[3,0,1]
# nums.sort()
# def missingNumber(nums):
#     for i in range(len(nums)+1):
#         if i in nums:
#             pass
#         else:
#             return i

# print(missingNumber(nums))


# nums=[3,0,1]
def missingNumber(nums):
    n=len(nums)
    pre_sum=sum(nums)
    exp_sum=(n*(n+1))//2
    return exp_sum-pre_sum

# print(missingNumber(nums))