import sys
sys.setrecursionlimit(10**6)
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    matrix=[list(map(int,input().split())) for i in range(n)]
    answer=0
    def dfs(l,r):
        if  l<0 or l>len(matrix)-1 or r<0 or r>len(matrix[0])-1 or matrix[l][r]==0:
            return 0
        p=matrix[l][r]
        matrix[l][r]=0
        return p+ dfs(l+1,r)+dfs(l,r+1)+dfs(l-1,r)+dfs(l,r-1)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                continue
            count=dfs(i,j)
            answer=max(answer,count)
    print(answer)





                
    
        