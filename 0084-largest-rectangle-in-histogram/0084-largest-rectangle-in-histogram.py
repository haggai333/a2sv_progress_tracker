class Solution(object):
    def largestRectangleArea(self, heights):
        stack=[]
        result=0
        size=len(heights)
        for i in range(size):
            min_index=i
            while stack and stack[-1][0]>heights[i]:
                h,prev=stack.pop()
                result=max(result,(i-prev)*h)
                min_index=min(min_index,prev)
            stack.append([heights[i],min_index])
            
        for h,i in stack:
            result=max(result,h*(size-i))
        return result
            


                



        