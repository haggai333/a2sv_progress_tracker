class Solution(object):
    def matrixReshape(self, mat, r, c):
        if len(mat)*len(mat[0])!=r*c:
            return mat
        temp=[]
        answer=[]
        for i in mat:
            for j in i:
                temp.append(j)
        for i in range(0, len(temp), c):
                answer.append(temp[i:i+c])
        return answer
            
            

        