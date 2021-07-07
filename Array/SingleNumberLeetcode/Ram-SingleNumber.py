#nums=[4,1,2,1,2]
# def single(l):     
#     d=[]           
#     for i in l:
#         if i not in d:
#             d.append(i)
#         else:
#             d.remove(i)
#     return d[0]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            n ^=i
        return n
