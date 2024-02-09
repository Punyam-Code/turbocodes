#Q3 Two Sum
 
 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(0,len(nums)):
            tar=target-nums[i]
            if tar in dic:
                return [dic[tar],i]
            else:
                dic[nums[i]]=i