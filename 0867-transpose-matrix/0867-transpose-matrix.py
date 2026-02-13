class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer=[]
        row=len(matrix)
        col=len(matrix[0])
        for i in range(col):
            answer.append([])
            for j in range(row):
                answer[i].append(matrix[j][i])
        return answer
                

        