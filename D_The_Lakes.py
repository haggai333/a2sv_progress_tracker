
t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    matrix=[list(map(int,input().split())) for i in range(n)]
    
    answer=0
    checked = [ [False] * m for _ in range(n)]
    dir=[(0,1),(1,0),(0,-1),(-1,0)]
    for i in range(n):
        for j in range(m):
            if not checked[i][j] and matrix[i][j]>0:
                stacks = [(i,j)]
                checked[i][j]=True
                total=0
                while stacks:
                    x , y = stacks.pop()
                    total+=matrix[x][y]
                    for p,q in dir:
                        nwi,nwj=x+p,y+q
                        if 0<=nwi<n and 0<=nwj<m and matrix[nwi][nwj]>0 and not checked[nwi][nwj]:
                            stacks.append((nwi,nwj))
                            checked[nwi][nwj]=True
                    
                answer=max(total,answer)
    print(answer)





                
    
        