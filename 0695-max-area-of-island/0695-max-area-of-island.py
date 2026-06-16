class Solution(object):
    def maxAreaOfIsland(self, grid):
        answer=0
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or  j>=len(grid[0]) or grid[i][j]==0:
                return 0
            grid[i][j]=0
            return 1 +dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    continue
                count=dfs(i,j)
                answer=max(answer,count)
        return answer

        