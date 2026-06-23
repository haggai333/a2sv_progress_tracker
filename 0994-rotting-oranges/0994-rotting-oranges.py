class Solution(object):
    def orangesRotting(self, grid):
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        answer=0
        queue=deque()
        contains=False
        time=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    contains=True
        if not contains:
            return 0
        while queue:
            size=len(queue)
            time+=1
            for _ in range(size):
                l,p=queue.popleft()
               
                for x,y in dir:
                    xi=l+x
                    yi=p+y
                    if xi>-1 and xi<len(grid) and yi>-1 and yi<len(grid[0]) and grid[xi][yi]==1:
                        grid[xi][yi]=2
                        queue.append((xi,yi))
                        answer=max(time,answer)
            
        for i in grid:
            for j in i:
                if j==1:
                    return -1
        return answer
                    
                    
                



                
        