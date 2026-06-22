class Solution(object):
    def floodFill(self, image, sr, sc, color):
        stack=deque()
        visited=set()
        stack.append((sr,sc))
        need=image[sr][sc]
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        while stack:
            i,j=stack.popleft()
            image[i][j]=color
            visited.add((i,j))
            for xi,yj in dirs:
                x=xi+i
                y=yj+j
                if y>-1 and y<len(image[0]) and x>-1 and x<len(image) and (x,y) not in visited and image[x][y]==need: 
                    stack.append((x,y))
        return image



        