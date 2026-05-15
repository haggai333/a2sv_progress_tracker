class Solution(object):
    def generate(self, numRows):
        answer=[[1]]
        for i in range(1,numRows):
            if i==1:
                answer.append([1,1])
                continue
            temp=[1]
            for j in range(0,i-1):
                temp.append(answer[i-1][j]+answer[i-1][j+1])
            temp.append(1)
            answer.append(temp)
        return answer


        