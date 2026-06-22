class Solution(object):
    def numIslands(self, grid):
        answer=0
        def bfs(i,j):
            queue=deque()
            queue.append((i,j))
            dir=[(1,0),(0,1),(-1,0),(0,-1)]
            while queue:
                x,y=queue.popleft()
                 
                for xi,xy in dir:
                    n=xi+x
                    p=xy+y
                    if n>-1 and n<len(grid) and p>-1 and p<len(grid[0]) and grid[n][p]!="0":
                        queue.append((n,p))
                        grid[n][p]="0"
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!="0":
                    answer+=1
                    bfs(i,j)
        
        return answer




                

                    
                    
                    

        