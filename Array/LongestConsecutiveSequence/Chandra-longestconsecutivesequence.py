class Solution:
    def longestConsecutive(nums):
        s=set(nums)
        longest_sequence=0
        for i in  nums:
            if (i-1) not in s:
                length=0
                while (i+length) in s:
                    length=length+1
                longest_sequence=max(length,longest_sequence)
        return longest_sequence
