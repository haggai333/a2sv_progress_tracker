class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        
        size=len(height)
        i=0
        j=size-1
        
        while j>i:
            if height[i]>=height[j]:
                k=(j-i)*min(height[i],height[j])
                area=max(area,k)
                j-=1 
                
            if height[i]<=height[j]:
                k=(j-i)*min(height[i],height[j])
                area=max(area,k)
                i+=1
        return area
        