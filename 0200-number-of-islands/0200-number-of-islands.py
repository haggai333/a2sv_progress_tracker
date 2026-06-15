class Solution(object):
    def numIslands(self, grid):
        visited=set()
        answer=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!="1" or (i,j) in visited:
                    continue
                answer+=1
                visited.add((i,j))
                stack=[]
                dirs=[[1,0],[0,1],[-1,0],[0,-1]]
                for p in dirs:
                    o=p[0]+i
                    u=p[1]+j
                    if o>-1 and o<len(grid) and u>-1 and u<len(grid[0]) and grid[o][u]=="1":
                        stack.append([o,u])
                while stack:
                    x,y=stack.pop()
                    visited.add((x,y))
                    for p in dirs:
                        o=p[0]+x
                        u=p[1]+y
                        if (o,u) in visited:
                            continue
                        if o>-1 and o<len(grid) and u>-1 and u<len(grid[0]) and grid[o][u]=="1":
                            stack.append([o,u])
        return answer


                

                    
                    
                    

        