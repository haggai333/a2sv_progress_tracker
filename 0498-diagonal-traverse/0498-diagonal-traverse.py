class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer=[]
        for i in range(len(mat[0])):
            y=i
            x=0
            temp=[]
            while  x < len(mat) and y >= 0:
                temp.append(mat[x][y])
                y-=1
                x+=1
            if i % 2 == 0:
                temp.reverse()
            answer+=temp
        p=len(mat[0])-1
        for j in range(1,len(mat)):
            y=p
            x=j
            temp=[]
            while x < len(mat) and y >= 0:
                temp.append(mat[x][y])
                y-=1
                x+=1
            if (p + j) % 2 == 0:
                temp.reverse()
            answer+=temp

        return answer

        