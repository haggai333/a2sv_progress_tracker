class Solution(object):
    def searchMatrix(self, matrix, target):
        l=0
        r=len(matrix)*len(matrix[0])-1
        n=len(matrix[0])
        while l<=r:
            mid=(l+r)//2
            value=matrix[mid//n][mid%n]
            if value<target:
                l=mid+1
            elif value>target:
                r=mid-1
            else:
                return True
        return False
        