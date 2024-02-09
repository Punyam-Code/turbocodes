#Q8 Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # duplicates must not be counted so use set
        num_set=set(nums)
        lsc=0
        for i in nums:
            # checking if sequence does not have left neighbour exist in the numset it is new sequence starting
            if (i-1) not in num_set:
                l=0
                while (i+l)in num_set:
                    l=l+1
                lsc=max(l,lsc)
        return lsc
        