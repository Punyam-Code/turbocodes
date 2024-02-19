           
#Q10 3Sum
#output must not have duplicates like here twice -1 in input will give two sets of samillar solution for 0th index -1 and 4th index -1 solution will be same so consider only one
#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Explanation: 
#nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#The distinct triplets are [-1,0,1] and [-1,-1,2]

# approach sort the list and pickl first element then rest can be solved like two sum but as it is sorted so we can use two pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#sorting so that we can remove all duplicate possible solution
        res=[]
        for i,v in enumerate(nums):
            if i>0 and v==nums[i-1]:# starting from condition that if we have the duplicate sequence again in the list after sorting
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                sum=v+nums[l]+nums[r]
                if sum<0:
                    l=l+1
                elif sum>0:
                    r=r-1
                else:
                    res.append([v,nums[l],nums[r]])
                    l=l+1
                    while nums[l]==nums[l-1]and l<r:
                        l=l+1
        return res
