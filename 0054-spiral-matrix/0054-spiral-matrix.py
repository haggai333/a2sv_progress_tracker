class Solution(object):
    def spiralOrder(self, matrix):
        answer=[]
        leftb=0
        rightb=len(matrix[0])-1
        downb=len(matrix)-1
        upb=0
        count=0
        while count<(len(matrix)*len(matrix[0])):
            for i in range(leftb,rightb+1):
                answer.append(matrix[upb][i])
                count+=1
            upb+=1
            for i in range(upb,downb+1):
                answer.append(matrix[i][rightb])
                count+=1
            rightb-=1
            if upb <= downb:
                for i in range(rightb,leftb-1,-1):
                    answer.append(matrix[downb][i])
                    count+=1
                downb-=1
            if leftb <= rightb:
                for i in range(downb,upb-1,-1):
                    answer.append(matrix[i][leftb])
                    count+=1
                leftb+=1
            

        return answer
        

        