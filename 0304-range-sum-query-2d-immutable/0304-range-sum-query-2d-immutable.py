class NumMatrix(object):

    def __init__(self, matrix):
        row,col=len(matrix),len(matrix[0])
        self.prefixmatrix=[[0]*(col+1) for r in range(row+1)]

        for r in range(row):
            prefix=0
            for c in range(col):
                prefix+=matrix[r][c]
                above=self.prefixmatrix[r][c+1]
                self.prefixmatrix[r+1][c+1]=prefix+above

        
        

    def sumRegion(self, row1, col1, row2, col2):
        return(
        self.prefixmatrix[row2+1][col2+1]
        -self.prefixmatrix[row1][col2+1]
        -self.prefixmatrix[row2+1][col1]
        +self.prefixmatrix[row1][col1])


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)