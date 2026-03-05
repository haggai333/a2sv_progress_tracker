class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        j=len(height)-1
        i=0
        while j>i:
            if height[i]>=height[j]:
                k=(j-i)*min(height[i],height[j])
                area=max(area,k)
                j-=1 
            else:
                k=(j-i)*min(height[i],height[j])
                area=max(area,k)
                i+=1
        return area
        