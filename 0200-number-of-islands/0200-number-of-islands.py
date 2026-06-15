class Solution(object):
    def numIslands(self, grid):
        visited=set()
        answer=0
        def dfs(i,j):
            if (i,j) in visited or i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]=="0":
                return
            visited.add((i,j))
            dirs=[[1,0],[0,1],[-1,0],[0,-1]]
            for o,p in dirs:
                dfs(i+o,j+p)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!="1" or (i,j) in visited:
                    continue
                answer+=1
                dfs(i,j)
        return answer


                

                    
                    
                    

        