class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Type1 To update inplace in a array we should use : 
        k=k%len(nums)
        nums[:]=(nums[len(nums)-k-1::-1]+nums[:len(nums)-k-1:-1])[::-1]
        #Type2
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]


    #Type3
    #     k =k% len(nums)
    #     self.reverse(nums, 0, len(nums) - 1)
    #     self.reverse(nums, 0, k - 1)
    #     self.reverse(nums, k, len(nums) - 1)

    # def reverse(self, nums: List[int], l: int, r: int) -> None:
    #     while l < r:
    #         nums[l], nums[r] = nums[r], nums[l]
    #         l += 1
    #         r -= 1