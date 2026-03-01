class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxi=0
        points.sort()
        for i in range(0,len(points)-1):
            maxi=max(maxi,(points[i+1][0]-points[i][0]))
        return maxi
        
        