class Solution(object):
    def transpose(self, matrix):
        answer=[]
        for i in range(len(matrix[0])):
            temp=[]
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            answer.append((temp))
        return answer
            