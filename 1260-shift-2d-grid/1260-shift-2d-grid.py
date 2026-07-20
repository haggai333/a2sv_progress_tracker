class Solution(object):
    def shiftGrid(self, grid, k):
        q=deque()
        m=len(grid)
        n=len(grid[0])
        k=k%(m*n)
        for i in grid:
            for j in i:
                q.append(j)
        grid=[]
        for i in range(k):
            q.appendleft(q.pop())
        
        while q:
            a=[]
            for i in range(n):
                print(1)
                a.append(q.popleft())
            grid.append(a)
        return grid
        