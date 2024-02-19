class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute force
        # res=0
        # for i in range(len(height)):
        #     for j in range(len(height)):
        #         area=(j-i)*min(height[i],height[j])
        #         res=max(res,area)
        # return res
        res=0
        l,r=0,len(height)-1
        while l<r:
            area=(r-l)*min(height[r],height[l])
            res=max(res,area)
            if height[l]<height[r]:
                l=l+1
            # elif height[l]>height[r]:
            #     r=r-1
            # else:                both elif and else are same
            #     # l=l+1 or
            #     r=r-1
            else:
                r=r-1
        return res